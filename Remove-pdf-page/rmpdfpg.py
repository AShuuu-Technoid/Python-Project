import os
from PyPDF2 import PdfFileWriter, PdfFileReader

def rmpdfpg():
    FileList = os.listdir("/Users/ashwin.m/Documents/scripts/python/removepdfpage")
    for fn in FileList:
        if fn.endswith(".pdf"):
            fnm=os.path.join("/Users/ashwin.m/Documents/scripts/python/removepdfpage",fn)
            pages_to_delete = [0] # page numbering starts from 0
            infile = PdfFileReader(fnm, 'rb')
            output = PdfFileWriter()
            for i in range(infile.getNumPages()):
                if i not in pages_to_delete:
                    p=infile.getPage(i)
                    output.addPage(p)
            with open(fnm, 'wb') as f:
                output.write(f)

if __name__ == "__main__":
    rmpdfpg()
