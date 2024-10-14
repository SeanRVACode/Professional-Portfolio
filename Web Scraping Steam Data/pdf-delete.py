from PyPDF2 import PdfReader,PdfWriter
from PyPDF2.generic import Destination


input_pdf_path = r"N:\Sean P Data Drops\SKLAR, RANDY A._2023_SOURCE DOCUMENTS_12.31.23 1040 SOURCE DOCUMENTS.pdf"
output_path = "./pdf_save.pdf"


reader = PdfReader(input_pdf_path)

writer = PdfWriter()

pages_to_exclude = [65,66]

page_mapping = {}
new_page_number = 0


for page_num in range(len(reader.pages)):
    if page_num not in pages_to_exclude:
        writer.add_page(reader.pages[page_num])
        page_mapping[page_num] 


with open(output_path,'wb') as output_file:
    writer.write(output_file)   