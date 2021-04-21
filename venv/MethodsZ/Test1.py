import csv
import re
from Util import tupleToNestedList, convert, intersection

f = open('C:/Users/Jodre/OneDrive/Desktop/CSV Files for candidates/InputFile.csv')

csv_f = csv.reader(f)

inputFilePostCode = []

for row in csv_f:
    inputFilePostCode.append(row)

f.close()

f = open('C:/Users/Jodre/OneDrive/Desktop/CSV Files for candidates/LondonPostcodes.csv')

csv_f = csv.reader(f)

LondonPostcodes = []

for row in csv_f:
    LondonPostcodes.append(row)

f.close()

intersecting = (intersection(LondonPostcodes, inputFilePostCode))

with open('intersection.csv', 'w', newline='') as f:
    thewriter = csv.writer(f, delimiter=",", lineterminator="\r\n")

    thewriter.writerows(intersecting)
    f.close


# QUESTION 2/
# convert nested list to tuple so it will accepted by set
intersecting = [tuple(l) for l in intersecting]
inputFilePostCode = [tuple(l) for l in inputFilePostCode]

intersectingSet = set(convert(intersecting))
inputFilePostCodeSet = set(convert(inputFilePostCode))

# take away the intersecting data  = inputfile reduced to 1000 values
inputFilePostCode = list(inputFilePostCodeSet - intersectingSet)

# convert tuples to string so we can use regex
inputFilePostCodeString = ('\n'.join(''.join(elems) for elems in inputFilePostCode))

# this return all the are the the format of the first postcode that are not in the intersecting data
# AN NAA
typeOnePostcode = re.findall(r'\b[A-Z]\d\s*\d[A-Z][A-Z]\b', inputFilePostCodeString)

# the first postcode pattern but not in the intersecting with London file
with open('firstPostcodePattern.csv', 'w', newline='') as f:
    thewriter = csv.writer(f, delimiter=",", lineterminator="\r\n")
    Alist = tupleToNestedList(typeOnePostcode)
    thewriter.writerows(Alist)
    f.close


# QUESTION 3/
#ANN NAA
typeTwoPostCode= re.findall(r'\b[A-Z]\d\d\s*\d[A-Z][A-Z]\b', inputFilePostCodeString)
#AAN NAA
typeThreePostCode= re.findall(r'\b[A-Z][A-Z]\d\s*\d[A-Z][A-Z]\b', inputFilePostCodeString)
#AANN NAA
typeFourPostCode= re.findall(r'\b[A-Z][A-Z]\d\d\s*\d[A-Z][A-Z]\b', inputFilePostCodeString)
#ANA NAA
typeFivePostCode= re.findall(r'\b[A-Z]\d[A-Z]\s*\d[A-Z][A-Z]\b', inputFilePostCodeString)
#AANA NAA
typeSixPostCode= re.findall(r'\b[A-Z][A-Z]\d[A-Z]\s*\d[A-Z][A-Z]\b', inputFilePostCodeString)


AllTypePostCodes =  typeOnePostcode + typeTwoPostCode + typeThreePostCode + typeFourPostCode + typeFivePostCode + typeSixPostCode

#Back to nested list
AllTypePostCodes = tupleToNestedList(AllTypePostCodes)

# convert nested list to tuple so it will accepted by set
AllTypePostCodes = [tuple(l) for l in AllTypePostCodes]

#Convert to set
AllTypePostCodesSet = set(convert(AllTypePostCodes))
inputFilePostCodeSet1 = set(convert(inputFilePostCode))



# take away all the post code types  = inputfile reduced to 1000 values
inputFilePostCodeErrors = list(inputFilePostCodeSet1 - AllTypePostCodesSet)

with open('inputFilePostCodeErrors.csv', 'w', newline='') as f:
    thewriter = csv.writer(f, delimiter=",", lineterminator="\r\n")
    #Alist = tupleToNestedList(inputFilePostCodeErrors)
    thewriter.writerows(inputFilePostCodeErrors)
    f.close


