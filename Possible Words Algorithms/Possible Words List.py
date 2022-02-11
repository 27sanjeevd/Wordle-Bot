f = open("sgb-words.txt", "r")


wordList = []

for x in f:
    wordList.append(x)


value = False

#a = green
#b = yellow
#c = grey

thisdict = {}
possibleLetters = []

while not value:
    userInput = input("Enter Word: ")
    wordCorrect = input("Enter Response: ")
    
    for x in range(len(wordCorrect)):
        if wordCorrect[x] == "a":
            thisdict[userInput[x]] = str(x)   
        if wordCorrect[x] == "b":
            if userInput[x] not in thisdict:
                temp = "";
                for y in range(5):
                    if y != x:
                        if temp == "":
                            temp += str(y)
                        else:
                            temp += " " + str(y)
                        thisdict[userInput[x]] = temp;
            else:

                temp = thisdict[userInput[x]].split(" ")
                temp1 = "";
                for z in temp:
                    if z != x:
                        if temp1 == "":
                            temp1 += str(z)
                        else:
                            temp1 += " " + str(z)

                thisdict[userInput[x]] = temp1      
        if wordCorrect[x] == "c":
            thisdict[userInput[x]] = ""           
    newList = []
    for x in wordList:
        check1 = True

        for y in thisdict:
            temp = thisdict[y]

            if temp == "":
                if y in x:
                    check1 = False

            if len(temp) == 1:
                if x[int(temp)] != y:
                    check1 = False
                    break
    

            if len(temp) > 1:
                temp1 = temp.split(" ")
                check2 = False
                for z in temp1:
                    if x[int(z)] == y:
                        check2 = True

                if not check2:
                    check1 = False

        if check1:
            newList.append(x);
    if len(newList) < 20:
        print(newList)
    print(len(newList))
    #value = True
    

print(thisdict)
