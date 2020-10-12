# extract_doc_info.py
import PyPDF2
from PyPDF2 import PdfFileReader

def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        pdfReader = PyPDF2.PdfFileReader(pdf_path)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
        page = pdfReader.getPage(0)
    txt =f
    """
    Information about {pdf_path}:

    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    """

    print(page)
    return information

if __name__ == '__main__':
    path = 'name.pdf'
    extract_information(path)
