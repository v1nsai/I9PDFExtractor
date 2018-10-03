import pandas as pd
from pandas.io.json import json_normalize
import sys
import json
from pathlib import Path
import re

## Test if incoming flowFile contains attestation data that needs to be added to the JSON and create a variable 'match'
flowFile = sys.stdin.read()
# m = re.search('(?<=}).*', flowFile)
# match = m.group(0)
# # Delete all text after the closing bracket so it is a valid JSON, then load as a JSON
# flowFile = re.sub('(?<=}).*', '', flowFile)
data = json.loads(flowFile)
# # If data was found merged with the JSON, add it to the JSON with the key 'Attestation'
# if len(match) > 0:
#     data['Attestation'] = match
df = json_normalize(data)

# Check for previous output and append to it or create a new output file
results_file = Path('/data/fast/hortonworks/PDF-Data-Extraction/output/results.csv')
if results_file.is_file():
    results = pd.read_csv('/data/fast/hortonworks/PDF-Data-Extraction/output/results.csv')
    results = results.append(df)
else:
    results = df

results.to_csv(sys.stdout, index=False)