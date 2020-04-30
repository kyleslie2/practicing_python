import csv
import gmplot

#The code of your four functions is below
#1
def convertFileDate(d):
    d = d[:-1]                                          #slice the last character off the string to remove the Z
    makingList = d.split("T")                           #split the list around the T to seperate the date and time
    makingTuple = tuple(makingList)                     #make a tuple out of the list
    return makingTuple                                  #return the tuple you've made!
# convertFileDate("2017-08-12T14:19:29Z")
# print(convertFileDate("2017-08-12T14:19:29Z"))

#3
def convertFileCoordinates(d):
    listItems = d.split(",")                            #split the string around the , to seperate the lat and long
    floatTuple = tuple(float(e) for e in listItems)     #convert each element of the list to a float and then a tuple
    return floatTuple                                   #return the tuple you've made!
# convertFileCoordinates("45.469807,12.50894")
# print(convertFileCoordinates("45.469807,12.50894"))

#5
# myString = input("Input a string of characters please> ")
def convertFileCallsign(d):
    stringLength = len(d)                               #counting length of str
    if stringLength > 3:                                #make a loop where if the string is longer than 3 chars...
        finalVar = d[:3]                                #splice to return first 3 chars of string
    else:
        finalVar = "null"                               #otherwise return string "null"
    return finalVar                                     #return the result of your if/else statement
# convertFileCallsign(myString)
# print(convertFileCallsign(myString))

#7
# anotherString = input("Input string of characters please> ")
def convertFileCallsign1(d):
    stringLength = len(d)                               #counting length of str
    if stringLength > 3:                                #make a loop where if the string is longer than 3 chars...
        finalVar = d[3:]                                #slice to return the last 3 chars of the string
    else:
        finalVar = "null"                               #otherwise return string "null"
    return finalVar                                     #return result of your if/else statement
# convertFileCallsign(anotherString)
# print(convertFileCallsign(anotherString))


# ======>DONE The following line prompts the user for the name of the output csv file and stores it in variable f1 (Python 3)
f1 = input("What do you want to call your new CSV file?>") + ".csv"

#open the file for writing and write the header line
wf = open(f1,'w')
wf.write("id,CallSign,ICAO,Flight,Date,Time,Latitude,Longitude,Altitude,Speed,Direction\n")
# ======>DONE The following line prompts the user for the name of the input csv file
#and stores it in variable f2 (Python 3)
f2 = input("What file do you want to open?>") + ".csv"

#open the file for reading
with open(f2,'rU') as f:
    reader = csv.reader(f)
    i = 1
    #Skip the first line
    next(reader,None)

    #row is a list of all elements in the csv line
    for row in reader:

        # ======>DONE call function convertFileDate on the date/time and store into a tuple t1
        utc = row[1]                                    #make variable for records in the column of index 1 in .csv
        t1 = convertFileDate(utc)
        # print(type(t1))

        cs = row[2]
        # ======>DONE call function convertFileCallsign on the variable cs and store into a variable csp1
        csp1 = convertFileCallsign(cs)
        # print(type(csp1))

        # ======> call function convertFileCallsign1 on the variable cs and store into a variable csp2
        csp2 = convertFileCallsign1(cs)

        # ======> call function convertFileCoordinates on the coordinates and store into a tuple t2
        coordinates = row[3]                            #make variable for records in the column of index 3 in .csv
        t2 = convertFileCoordinates(coordinates)
        #store altitude, speed and direction
        alt = row[4]
        spd = row[5]
        dir = row[6]

        #create the line to write to the file
        strToPrint = str(i)+ "," + cs + "," + csp1 + "," +csp2 + "," + t1[0] + "," + t1[1] + "," + str(t2[0]) + "," + str(t2[1]) + "," + alt + "," + spd + "," + dir + "\n"
        wf.write(strToPrint)

        # ======>DONE increment line counter by 1
        i = i + 1

#close the output file
wf.close()

with open(f1,'rU') as f:
    reader = csv.reader(f)
    next(reader, None)
    lat=[]
    lon=[]
    for row in reader:
        # ======> convert the read latitude to a float and store it into a variable lt
        readLat = row[6]                               #read from index 6 (latitude column) in .csv
        lt = float(readLat)
        # ======> convert the read longitude to a float and store it into a variable lg
        readLon = row[7]                              #read from index 7 (longitude column) in .csv
        lg = float(readLon)
        # ======> add lt to the latitude list lat
        lat.append(lt)
        # ======> add lg to the longitude list lon
        lon.append(lg)

#initialize the plot
gmap = gmplot.GoogleMapPlotter(lat[0],lon[0],5)
gmap.scatter(lat, lon, 'cornflowerblue', edge_width=4,marker=False)

#Create the html file
gmap.draw('map.html')
