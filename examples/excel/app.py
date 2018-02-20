from automagica import *

"""
Reads information from one Excel file and writes it to the other.
"""

# Read information from example.xlsx in cell A1
workbook = OpenExcelWorkbook('example.xlsx')
worksheet = workbook.active
cell_content = worksheet['A1'].value

# Write information to new file
new_workbook = NewExcelWorkbook()
new_worksheet = new_workbook.active
new_worksheet['A1'] = cell_content

new_workbook.save('result.xlsx')

