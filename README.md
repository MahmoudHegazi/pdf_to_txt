# pdf_to_TXT

#install pyDF2
pip install PyPDF2

# importing all the required modules
import PyPDF2

# creating an object 
file = open('example.pdf', 'rb')

# creating a pdf reader object
fileReader = PyPDF2.PdfFileReader(file)

# print the number of pages in pdf file
print(fileReader.numPages)


https://automatetheboringstuff.com/chapter13/
https://stackoverflow.com/questions/64142307/how-to-extract-only-specific-text-from-pdf-file-using-python



```python


# extract_doc_info.py

from PyPDF2 import PdfFileReader

def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

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

    print(information.producer)
    return information

if __name__ == '__main__':
    path = 'name.pdf'
    extract_information(path)
    
 ```

https://pythonhosted.org/PyPDF2/PdfFileReader.html
