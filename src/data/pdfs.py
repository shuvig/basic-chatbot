from PyPDF2 import PdfReader


class PDFManager:
    def __init__(self):
        pass

    def get_text_from_pdf(self, pdf) -> str:
        text: str = ""
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()

        return text

    def get_text_from_multiple_pdfs(self, pdfs) -> str:
        text: str = ""
        for pdf in pdfs:
            text += self.get_text_from_pdf(pdf)
        return text