FILES
There is separate util.py file with functions. 
Test1.py is the main script.
For you to run it, you need to put in the paths names to 
the data on line 5 (InputFile) and line 16(London PostCodes)

ASSUMPTIONS
The only assumption i made was to give
unlimited white space between the first and second
half of the postcode.

PROCESS
1/ Intersection = intersection of LondonPostcodes and InputFile and save file. 
2/ A= convert Intersection set
3/ B= convert InputFile to set
4/ Inputfile = B-A
5/ Convert InputFile to string for regex
6/ C= Findall first postcode and save that file
7/ D= Findall for all other postscodes
8/ AllValidPostCodes = C + D
9/ E = Convert AllValidPostCodes to nested list then to set
10/ F= Convert InputFile to set
11/ Errors = F - E
12/ Save Errors file

TESTING
There is also a folder called Testing
where i took out 30 input values and did a manual check.
There is 'readme' in the Testing Folder.

GOING FORWARD
I understand that i could look to delete non
alphanumeric characters and recheck if valid
but not done this. This is the next step.

Also, i understand that the regex is verbose. 

Also, there is discrepency regards 19 rows.
I have 1500 starting values = 500 intersecting +  414 inValid Postcodes + 586 Valid Postcode values that are non-intersecting with London.
I am sure there is an error here.

OUTPUT
The three CSV files are
intersecting.csv which is the London Postcode matches
firstPostcodePattern.csv which is the first pattern on the list

NOTE
Note, i did not good answers for postcode
problems or postcode regex. 



 

 