from automagica import *

# Put the links google returns in a list and name it "president_links".
president_links = GetGoogleSearchLinks("us presidents")

# Write the links to a .txt file and save it at a new path.
WriteListToFile(president_links, "C:\\Users\\Bob\\Desktop\\US_Presidents.txt")

# Open the newly made .txt file.
OpenFile("C:\\Users\\Bob\\Desktop\\US_Presidents.txt")