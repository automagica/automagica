def read_text(file_path):
    """Extracts the text from a PDF

    :param file_path: Path to the PDF (either relative or absolute)
    :return: The text from the PDF
    """
    from PyPDF2 import PdfFileReader

    text = ''

    with open(file_path, 'rb') as f:
        reader = PdfFileReader(f)
        for i in range(reader.numPages):
            page = reader.getPage(i)
            text += page.extractText()

    return text

def join(file_paths, output_path):
    """Merges multiple PDFs into a single file

    :param file_paths: List of paths to PDF files
    """
    from PyPDF2 import PdfFileMerger, PdfFileReader

    merger = PdfFileMerger()
    for file_path in file_paths:
        with open(file_path, 'rb') as f:
            merger.append(PdfFileReader(f))

    merger.write(output_path)
 
def extract_page_range(file_path, start_page, end_page, output_path):
    """Extracts a particular range of a PDF to a separate file

    :param file_path: Path to the PDF (either relative or absolute)
    :param start_page: Page number to start from, with 0 being the first page
    :param end_page: Page number to end with, with 0 being the first page
    """
    from PyPDF2 import PdfFileMerger, PdfFileReader

    with open(file_path, 'rb') as f:
        reader = PdfFileReader(f)
        writer = PdfFileWriter()

        for i in range(start_page, end_page):
            writer.addPage(reader.getPage(i))

        with open(output_path, 'wb') as f:
            writer.write(f)

def extract_images(file_path):
    """Save a specific page from a PDF as an image
    Credits to user Sylvain on Stackoverflow (https://stackoverflow.com/a/34116472)
    """
    from PyPDF2 import PdfFileReader
    from PIL import Image

    with open(file_path, "rb") as f:
        reader = PdfFileReader(f)
        for i in range(reader.getNumPages()):
            page = reader.getPage(i)
            objects = page['/Resources']['/XObject'].getObject()

            for obj in objects:
                if objects[obj]['/Subtype'] == '/Image':
                    size = (objects[obj]['/Width'], objects[obj]['/Height'])
                    data = objects[obj].getData()

                    if objects[obj]['/ColorSpace'] == '/DeviceRGB':
                        mode = "RGB"
                    else:
                        mode = "P"

                    if objects[obj]['/Filter'] == '/FlateDecode':
                        img = Image.frombytes(mode, size, data)
                        img.save(obj[1:] + ".png")

                    elif objects[obj]['/Filter'] == '/DCTDecode':
                        img = open(obj[1:] + ".jpg", "wb")
                        img.write(data)
                        img.close()

                    elif objects[obj]['/Filter'] == '/JPXDecode':
                        img = open(obj[1:] + ".jp2", "wb")
                        img.write(data)
                        img.close()

def save_page_as_image(file_path, page_number):
    """
    TODO
    """
    pass

def add_text_watermark(file_path, text, font='Helvetica-Bold', size=36):
    """
    TODO
    """
    pass


def add_image_watermark(folder_path, text='Automagica', watermark_image_path=''):
	"""
    TODO
	Open a directory containing .pdf files. All files in directory will be marked.
	Fill in text if you want to watermark with text.
	Fill in picture_path if you want to watermark with image.
	"""
	from reportlab.pdfgen import canvas
	from PyPDF2 import PdfFileWriter, PdfFileReader
	import os

	picture_path = 'company_logo.png'
	# Folder in which PDF files will be watermarked. (Could be shared folder)
	folder_path = './mydir'

	c = canvas.Canvas('watermark.pdf')
    if picture_path:
        c.drawImage(picture_path, 15, 15)
        
	if text:
		c.setFontSize(22)
		c.setFont('Helvetica-Bold', 36)
		c.drawString(15, 15,text)

	c.save()
	watermark = PdfFileReader(open("watermark.pdf", "rb"))
	
	for file in os.listdir(folder_path):
		if file.endswith(".pdf"):
	output_file = PdfFileWriter()
	input_file = PdfFileReader(open(folder_path + '/'+ file, "rb"))

	page_count = input_file.getNumPages()

	for page_number in range(page_count):
	   input_page = input_file.getPage(page_number)
	   input_page.mergePage(watermark.getPage(0))
	   output_file.addPage(input_page)
	output_path = folder_path + '/'+ file.split('.pdf')[0] + '_watermarked' + '.pdf'
	
	with open(output_path, "wb") as outputStream:
	   output_file.write(outputStream)
