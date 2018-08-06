import os
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
import sys

os.chdir(r'C:\Users\Andrew Riffle\PycharmProjects\I9PDFExtractor\nocr')

# Open and read the pdf file in binary mode
# fp = open('2011_i9_test_noPIV.pdf', "rb")
fp = sys.stdin.buffer.read()

# Create parser object to parse the pdf content
parser = PDFParser(fp)

# Store the parsed content in PDFDocument object
document = PDFDocument(parser)

# Check if document is extractable, if not abort
if not document.is_extractable:
    raise PDFTextExtractionNotAllowed
