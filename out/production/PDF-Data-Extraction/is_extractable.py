from sys import stdin, stdout
from io import BytesIO
import PyPDF2

# Open and read the pdf file in binary mode
fp = stdin.buffer.read()
fp = BytesIO(fp)
# fp = open(r'testfiles/ver07_marvin_martian.pdf', 'rb')

# Attempt to extract text from the first page
pdf = PyPDF2.PdfFileReader(fp)
page = pdf.getPage(0)
content = page.extractText()

# If more than 5 characters are extracted, document is extractable
if len(content) < 5:
    raise ValueError('Not extractable')

# Need to figure out how to do this properly, for now can just use did or did not error to route
# if len(content) > 4:
    # raise ValueError('Extractable')