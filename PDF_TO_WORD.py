from pdf2docx import Converter

pdf_file = "your_pdf_file.pdf"
docx_file = "your_docx_file.docx"

converter = Converter(pdf_file)
converter.convert(docx_file)
converter.close()