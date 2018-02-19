from automagica import *

"""
Opens a template Word document, replaces a template with content and saves as a new file.
"""

document = OpenWordDocument('example.docx')

new_document = ReplaceText(document, text='[template]', replace_with='invoice 123456')

new_document.save('result.docx')