from sys import stdin, stdout
from io import BytesIO
from os import system, chdir
import PyPDF2

# Open and read the pdf file in binary mode
fp = stdin.buffer.read()
fp = BytesIO(fp)
# fp = open(r'testfiles/ver07_marvin_martian.pdf', 'rb')

# Attempt to decrypt and extract text from the first page
pdf = PyPDF2.PdfFileReader(fp)
if pdf.isEncrypted:
    chdir(r'/data/fast/hortonworks/PDF-Data-Extraction/nocr/testfiles/decrypt')
    temp = open('temp.pdf', 'wb')
    temp.write(fp.getvalue())
    system("qpdf --password='' --decrypt temp.pdf temp_decrypted.pdf; rm temp.pdf")
    infile = open('temp_decrypted.pdf', 'rb')
    pdf = PyPDF2.PdfFileReader(infile)
    system('rm temp_decrypted.pdf')

# Write the unencrypted PDF to stdout
pdfbytes = BytesIO()
writer = PyPDF2.PdfFileWriter()
for i in range(pdf.getNumPages()):
    writer.addPage(pdf.getPage(i))
writer.write(pdfbytes)
stdout.buffer.write(pdfbytes.getvalue())
