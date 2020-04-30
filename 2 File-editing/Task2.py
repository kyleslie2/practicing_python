#Task 2

import csv

openedCSV = open(input("Type the name of your csv file") +".csv", "r")


reader = csv.reader(openedCSV)
next(reader, None)

myList = list(reader)

print(myList)

openedCSV.close()

#This returns a list of all the lines from the csv that was imported. Not sure how to incorporate the code from week8.py



