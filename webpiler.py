import os
import sys

#path, file, contents, tag
partList = []
rootdir = "./../html"
partsDir = "./../html_parts"
outputDir = "./../output/"


    
# We get the list of html parts
for root, subFolders, files in os.walk(partsDir):
    for file in files:
        file_name, file_extension = os.path.splitext(file)

        
        fullPath = os.path.join(root, file)
        partFile = open(fullPath)
        tag = "<" + file_name + file_extension +  ">"
        partList.append((fullPath, os.path.splitext(fullPath)[0].replace(rootdir, ""), partFile.read(), tag))
        finalFileName = outputDir + file 
        partFile.close()


# We load in the html pages
for root, subFolders, files in os.walk(rootdir):
    for file in files:
        file_name, file_extension = os.path.splitext(file)

        fullPath = os.path.join(root, file)
        finalFileName = outputDir + file 

        outfile = open(finalFileName, mode='w+', encoding="utf-8")

        # We copy the html part contents into the pages when <*.html> is tagged
        infile = open(fullPath, 'r', encoding="utf-8")

        outputText = infile.read()

        # Close the input file
        infile.close()

        for part in partList:
            outputText = outputText.replace(part[3], part[2])
        
        outfile.write(outputText)
        # We close the output file
        outfile.close()