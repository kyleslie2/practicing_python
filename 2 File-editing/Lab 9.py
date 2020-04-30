#Part 1

import csv

girlscsv = open("2000_GirlsNames.csv", "w")
boyscsv = open("2000_BoysNames.csv","w")

def Girls():
    with open("2000_GirlsNames.txt", "r") as f:
        girlscsv.write("Name, Count \n")
        for line in f:
            l = line.split(' ')
            girlscsv.write(l[0] + ',' + l[1])


def Boys():
    with open("2000_BoysNames.txt", "r") as f:
        boyscsv.write("Name, Count \n")
        for line in f:
            l = line.split(' ')
            boyscsv.write(l[0] + ',' + l[1])

Boys()
Girls()

