
from automagica import *


# Put the president names of the first column in a list.
names = ExcelPutColumnInList("C:\\Users\\Bob\\Downloads\\USPresidents.xlsx", "A2","A45")

# Create for every president a folder with his name and save a .txt file in that folder with his extra information.
for name in names:
    CreateFolder("C:\\Users\\Bob\\Documents\\Presidents\\" + name)
    row = names.index(name) + 2
    data = ExcelPutRowInList("C:\\Users\\Bob\\Downloads\\USPresidents.xlsx", "B"+str(row), "H" + str(row))
    WriteListToFile(data, "C:\\Users\\Bob\\Documents\\Presidents\\" + name + "\\" + name + ".txt")


