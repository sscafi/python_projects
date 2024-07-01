from pdf2docx import Converter

# Define input and output file paths
pdf_file = "your_pdf_file.pdf"    # Path to the PDF file to convert
docx_file = "your_docx_file.docx" # Desired path for the output DOCX file

# Initialize a Converter object with the input PDF file
converter = Converter(pdf_file)

# Convert the PDF file to DOCX format
converter.convert(docx_file)

# Close the Converter object to release resources
converter.close()
