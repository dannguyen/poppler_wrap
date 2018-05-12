class PdfDoc():
    def __init__(self, filename):
        self.filename = filename
        self.pages = []

    def page_count(self):
        return len(self.pages)


