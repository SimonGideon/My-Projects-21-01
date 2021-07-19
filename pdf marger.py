from PyPDF2 import PdfFileMerger
pdfs = ['D:\DESKTOP\mmm\Simon Gideon Mnayi - Resume.pdf', 'D:\DESKTOP\mmm\Motivation Letter.pdf', 'D:\DESKTOP\mmm\RESULTS SLIP.pdf']
merger = PdfFileMerger()
for pdf in pdfs:
    merger.append(pdf)
merger.write("result.pdf")
merger.close()