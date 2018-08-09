import pandas as pd
from pandas.io.json import json_normalize
import sys
import json
from pathlib import Path

# Put the incoming FlowFile into a dataframe
flowFile = sys.stdin.read()
data = json.loads(flowFile)
df = json_normalize(data)

# Check for previous output and append to it or create a new output file
results_file = Path('/data/fast/hortonworks/I9PDFExtractor/nocr/results.csv')
if results_file.is_file():
    results = pd.read_csv('/data/fast/hortonworks/I9PDFExtractor/nocr/results.csv')
    results = results.append(df)
else:
    results = df

# results.to_csv('/data/fast/hortonworks/I9PDFExtractor/nocr/results.csv', index=False)

results.to_csv(sys.stdout, index=False)

# This works but its pretty hideous
# results_csv = open('results.csv', 'w')
# csvwriter = csv.writer(results_csv)
#
# csvwriter.writerow(data.keys())
# csvwriter.writerow(data.values())
# results_csv.close()
#
# results_pd = pd.read_csv('results.csv', sep=',')
# results_pd.to_csv('test.csv')

