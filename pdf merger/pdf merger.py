from PyPDF2 import PdfFileReader, PdfFileMerger, PdfFileWriter

f1 = PdfFileReader("pdf merger\pdf1.pdf")
f2 = PdfFileReader("pdf merger\pdf2.pdf")
o = PdfFileMerger()
o.append(f1)
o.append(f2)
o.write(f"pdf merger\merged.pdf")
