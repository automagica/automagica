from automagica import *

"""
Opens a template Word document, replaces a template with content and saves as a new file.
"""

document = OpenWordDocument('example.docx')

new_document = ReplaceText(document, text='[template]', replace_with='invoice 123456')

new_document.save('result.docx')

"""
Opens the new file and saves it as PDF (all in the background).
This only works on Windows with Microsoft Office installed!
"""

import os

full_path_word_file = os.path.join(os.getcwd(), 'result.docx')

full_path_pdf_file = full_path_word_file.replace('.docx', '.pdf')

ConvertWordToPDF(word_filename=full_path_word_file, pdf_filename=full_path_pdf_file)
