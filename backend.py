from PyPDF2 import PdfFileWriter, PdfFileReader
import os
import time
# from gui import entries

class Backend :
    def __init__(self, start, end) -> None:
        self.start = int(start)  # if not type(start) == str else 0
        self.end = int(end)  # if not type(end) == str else 0
        self.pages = [i for i in range(start - 1, end)]
        self.hrn()
        self.div10()

    def hrn(self):
        with open("pages.pdf", "rb") as f:
            reader = PdfFileReader(f)
            writer = PdfFileWriter()
            # rest_writer = PdfFileWriter()

            for page in range(len(reader.pages)):
                if page in self.pages:
                    writer.addPage(reader.getPage(page))
                # else:
                #     rest_writer.addPage(reader.getPage(page))

            # with open("temp/file.pdf", "wb") as f:
            with open(os.path.join("temp", "file.pdf"), "wb") as f:
                writer.write(f)

            # with open(os.path.join("temp", "rest.pdf"), "wb") as f:
            #     rest_writer.write(f)

    def div10(self):
        with open("pages.pdf", "rb") as f:
            reader = PdfFileReader(f)
            writer = PdfFileWriter()
            rest_writer = PdfFileWriter()
            pdfs = []
            pages_in_pdf = len(reader.pages)
            remaining = pages_in_pdf - self.end

            for i in range(self.start, self.end):
                writer.addPage(reader.getPage(i))
            for i in range(self.end, pages_in_pdf):
                rest_writer.addPage(reader.getPage(i))

            with open("temp/{}.pdf".format(self.start), "wb") as f:
                writer.write(f)

            with open("temp/{}.pdf".format(self.end), "wb") as f:
                rest_writer.write(f)

    def work(self):
        self.div10()
        time.sleep(1)
        for file in os.listdir("temp"):
            if file.endswith(".pdf"):
                os.startfile(os.path.join("temp", file))


if __name__ == "__main__":
    backend  = Backend ()
