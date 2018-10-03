from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback
import json
import re

# Define a subclass of StreamCallback for use in session.write()
class PyStreamCallback(StreamCallback):
    def __init__(self):
        pass

    def process(self, inputStream, outputStream):
        # Get the JSON from the flowfile and put it into a Python dict
        text = IOUtils.toString(inputStream, StandardCharsets.UTF_8)
        # Detect if the attestation is attached to the JSON string before loading it as a Python dict
        # Attached after the JSON
        m = re.search('}(.*)', text)
        match1 = m.group(1)
        # Attached before the JSON
        m = re.search('(.*){', text)
        match2 = m.group(1)
        if match1:
            # Delete all text after the closing bracket so it is a valid JSON, then load as a JSON
            text = re.sub('}.*', '}', text)
            data = json.loads(text)
            data['Attestation'] = match1
        if match2:
            # Delete all text before the opening bracket so it is a valid JSON, then load as a JSON
            text = re.sub('.*{', '{', text)
            data = json.loads(text)
            data['Attestation'] = match2
        else:
            data = json.loads(text)

        if not data['File']:
            # Grab the filename
            filename = flowFile.getAttribute('filename')
            data['File'] = filename
            # Parse out the sub box
            m = re.search('SB(\d+)\s(\d+)\.pdf', filename)
            # Checks if the filename matches the pattern for testing files, otherwise ignores adding
            if m:
                data['Box'] = 1 #Has to be hardcoded
                data['Sub-box'] = m.group(1)
                data['Page'] = m.group(2)

        data = json.dumps(data)

        outputStream.write(bytearray(data.encode('utf-8')))


# end class
flowFile = session.get()
if (flowFile != None):
    flowFile = session.write(flowFile, PyStreamCallback())
    session.transfer(flowFile, REL_SUCCESS)
else:
    session.transfer(flowFile, REL_FAILURE)
# implicit return at the end
