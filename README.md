# pdf_to_txt

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
