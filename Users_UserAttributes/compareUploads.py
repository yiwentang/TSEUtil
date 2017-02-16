#
#  --- TSEUtil ---
#  Section: Users/User Attributes
#  
#  Description:
#    This is used to compare whether a file upload worked by taking two files:
#  1) File 1: Full Path of Original Upload File of Users
#  2) File 2: Full Path of Comparison File of Users
#  3) OutPutFile: Full path of differences in the two files.
# 
#  How To Use:
#  1) Change the strings below to location of file1Location, file2Location, and outPutFileLocationAndName with full path
#  2) Run the script (open terminal to script location)
#      - If script was on desktop it would look like this:
#          - cd ~/Desktop
#          - python compareUploads.py
#      
#  Author: Kyle Cote


import csv
import operator

#Make Sure to put the full path
file1Location = '/Users/kylecote/Desktop/zendesk_content/OfferUp/file1.csv'
file2Location = '/Users/kylecote/Desktop/zendesk_content/OfferUp/file2.csv'
outPutFileLocationAndName = '/Users/kylecote/Desktop/zendesk_content/OfferUp/missingUsers3.csv'


masterDict = dict()

#Add items in File1
with open(file1Location) as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        str_row0 = str(row[0])
        if str_row0 in masterDict:
            print('Duplicate user %s' % str_row0)
        else:
            masterDict[str_row0] = 1

#Add diffs from two files and spits out missing users between two files in outPutFileLocationAndName
with open(file2Location) as compareFile:
    with open(outPutFileLocationAndName,'w') as writeFile:
        writer = csv.writer(writeFile)
        reader = csv.reader(compareFile)
        for row in reader:
            str_row0 = str(row[0])
            if str_row0 not in masterDict:
                writer.writerow([str_row0])
