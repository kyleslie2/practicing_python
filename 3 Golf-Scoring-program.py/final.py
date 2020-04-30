def getHolesPar ():
    i = 0
    parList = []
    while (i <= 8):
        x = input("What is the par for this hole?> ")
        i += 1

        if (x == "3"):
            parList.append(x)

        elif x == "4":
            parList.append(x)
        elif x == "5":
            parList.append(x)
        else:
            print("That is not a valid par")
    return parList

parList = getHolesPar()

#

def getPlayerScore():
    score1 = input("what was your score on hole 1 (must be a positive #)?> ")
    score2 = input("what was your score on hole 2 (must be a positive #)?> ")
    score3 = input("what was your score on hole 3 (must be a positive #)?> ")
    score4 = input("what was your score on hole 4 (must be a positive #)?> ")
    score5 = input("what was your score on hole 5 (must be a positive #)?> ")
    score6 = input("what was your score on hole 6 (must be a positive #)?> ")
    score7 = input("what was your score on hole 7 (must be a positive #)?> ")
    score8 = input("what was your score on hole 8 (must be a positive #)?> ")
    score9 = input("what was your score on hole 9 (must be a positive #)?> ")
    scoreString = (score1+","+score2+","+score3+","+score4+","+score5+","+score6+","+score7+","+score8+","+score9)
    scoreList = scoreString.split(",")
    scoreList = [int(i) for i in scoreList]
    return scoreList

scoreList= getPlayerScore()





# # #Eagles(-2), Birdies (-1), Pars (0), Bogeys (+1), Double Bogeys (+2), Other (3+)
# parList = [4,5,4,3,3,3,4,5,4]
# scoreList = [3,6,1,4,4,3,5,8,2]

def getStats(parList, scoreList):
    #counter to iterate through lists
    i = 0
    #empty list
    finalList = [0,0,0,0,0,0]

    #while loop for the list to iterate through scores (9 times)
    while i<len(scoreList):
        i += i
        for e in range(len(parList)):
            #for pars
            if scoreList[e] == parList[e]:
                count = (finalList[2] + 1)
                finalList[2] = count

            elif scoreList[e] != parList[e]:
                if scoreList[e] - parList[e] > 0:
                    extraStrokes = scoreList[e] - parList[e]

                    if extraStrokes == 1:
                        count = finalList[3] + 1
                        finalList[3] = count

                    elif extraStrokes == 2:
                        count = finalList[4] + 1
                        finalList[4] =count

                    elif extraStrokes >= 3:
                        count = finalList[5] + 1
                        finalList[5] = count

                else:
                    goodScores = parList[e] - scoreList[e]
                    if goodScores == 2:
                        count = finalList[0] + 1
                        finalList[0]= count

                    elif goodScores == 1:
                        count = finalList[1] + 1
                        finalList[1]= count

                    elif goodScores >=3:
                        count = finalList[5] + 1
                        finalList[5]= count

        else:
            finalTuple = tuple(finalList)
            return finalTuple

print(getStats(parList, scoreList))


# listOfPars = [3,4,5,4,5,3,4,5,3]
def getCoursePar(listOfPars):
    totalPar = listOfPars[0]+listOfPars[1]+listOfPars[2]+listOfPars[3]+listOfPars[4]+listOfPars[5]+listOfPars[6]+listOfPars[7]+listOfPars[8]
    return totalPar

getCoursePar(listOfPars)


listOfScores = [5,5,5,3,4,5,4,5,3]
def getScore(listOfScores):
    totalScore = listOfScores[0]+listOfScores[1]+listOfScores[2]+listOfScores[3]+listOfScores[4]+listOfScores[5]+listOfScores[6]+listOfScores[7]+listOfScores[8]
    return totalScore

getScore(listOfScores)





















