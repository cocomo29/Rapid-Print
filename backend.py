from PyPDF2 import PdfFileWriter, PdfFileReader
import os
# import time
# from gui import entries


class Backend:
    def __init__(self,start,end) -> None:
        self.start = int(start) if not type(start) == str else 0
        self.end = int(end) if not type(end) == str else 0
        self.pages = [i for i in range(start, end)]

    def divider(self):
        with open("rapid.pdf", "rb") as f:
            reader = PdfFileReader(f)
            writer = PdfFileWriter()
            # rest_writer = PdfFileWriter()
            pdfs = []
            pages_in_pdf = len(reader.pages)
            # mid = pages_in_pdf // 2
            
            for i in range(0, pages_in_pdf, 10):
                writer = PdfFileWriter()
                for j in range(i, i + 10):
                    if j < self.end:
                        writer.addPage(reader.getPage(j))
                pdfs.append(writer)

            for i, pdf in enumerate(pdfs):
                with open(f"temp/file{i+1}.pdf", "wb") as f:
                    pdf.write(f)
            
        

    def Print(self):
        self.divider()
        # time.sleep(1)
        for file in os.listdir("temp"):
            if file.endswith(".pdf"):
                os.startfile(os.path.join("temp", file))
                break

if __name__ == "__main__":
    backend = Backend()

#fix broken pdf with qpdf
#qpdf --repair-file broken.pdf fixed.pdf
