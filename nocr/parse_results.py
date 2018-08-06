import pandas as pd
from pandas.io.json import json_normalize
import os
import json
import csv

os.chdir(r'C:\Users\Andrew Riffle\PycharmProjects\I9PDFExtractor\nocr')

with open('results.json') as f:
    data = json.load(f)

df = json_normalize(data)
df.to_csv('df.csv')






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
