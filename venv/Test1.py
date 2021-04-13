import csv
import re

f = open('C:/Users/Jodre/OneDrive/Desktop/CSV Files for candidates/InputFile.CSV')

csv_f = csv.reader(f)

inputFilePostCode = []

for row in csv_f:
    inputFilePostCode.append(row)

# print (inputFilePostCode)

f.close()

f = open('C:/Users/Jodre/OneDrive/Desktop/CSV Files for candidates/LondonPostcodes.csv')

csv_f = csv.reader(f)

LondonPostcodes = []

for row in csv_f:
    LondonPostcodes.append(row)

# print (LondonPostcodes)

f.close()

print(len(inputFilePostCode))
print(len(LondonPostcodes))


def convert(list):
    return tuple(list)


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


intersecting = (intersection(LondonPostcodes, inputFilePostCode))

# with open('intersection.csv', 'w', newline='') as f:
#     thewriter = csv.writer(f, delimiter=",", lineterminator="\r\n")
#
#     thewriter.writerows(intersecting)
#     f.close


# print (len(intersecting))

# convert nested list to tuple so it will accepted by set
intersecting = [tuple(l) for l in intersecting]
inputFilePostCode = [tuple(l) for l in inputFilePostCode]

intersectingSet = set(convert(intersecting))
inputFilePostCodeSet = set(convert(inputFilePostCode))
#
# print (len(inputFilePostCode))
# final = inputFilePostCode.difference(intersecting)
# print(len(final))

# take away the intersecting data
inputFilePostCode = list(inputFilePostCodeSet - intersectingSet)
# inputfile reduced to 1000 values
print(len(inputFilePostCode))

# print(inputFilePostCode)

#####################################

# convert tuples to string so we can use regex
inputFilePostCode = ('\n'.join(''.join(elems) for elems in inputFilePostCode))
# print (inputFilePostCode)

# this return all the are the the format of the first postcode
tuples = re.findall(r'[A-Z]\d\s*\d[A-Z][A-Z]', inputFilePostCode)
# print (tuples)  ## [('alice', 'google.com'), ('bob', 'abc.com')]
# for tuple in tuples:
#     print (tuple[0])  ## username
#     print (tuple[1])  ## host

print(len(tuples))

# convert tuples to string so we can use regex
intersecting = ('\n'.join(''.join(elems) for elems in intersectingSet))
# how many that follow the first pattern are in the intersecting set.
tuples = re.findall(r'[A-Z]\d\s*\d[A-Z][A-Z]', intersecting)
print(tuples)  ## [('alice', 'google.com'), ('bob', 'abc.com')]
# for tuple in tuples:
#     print (tuple[0])  ## username
#     print (tuple[1])  ## host

print(len(tuples))
