from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback
import json

# Define a subclass of StreamCallback for use in session.write()
class PyStreamCallback(StreamCallback):
    def __init__(self):
        pass

    def process(self, inputStream, outputStream):
        text = IOUtils.toString(inputStream, StandardCharsets.UTF_8)
        ffjson = json.loads(text)
        ffjson['File'] = flowFile.getAttribute('filename')

        ffjson = json.dumps(ffjson)

        outputStream.write(bytearray(ffjson[::-1].encode('utf-8')))


# end class
flowFile = session.get()
if (flowFile != None):
    flowFile = session.write(flowFile, PyStreamCallback())
# implicit return at the end