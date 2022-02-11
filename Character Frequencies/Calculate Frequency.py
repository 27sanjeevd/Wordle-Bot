f = open("sgb-words.txt", "r")


wordList = []

for x in f:
    wordList.append(x)
    
def split(word):
    return [char for char in word]

amounts = [[0 for x in range(26)] for y in range(5)]
check1 = True

for x in wordList:
    temp = split(x)
    if check1:
        for y in range(len(temp)):
            if y < 5:
                amounts[y][ord(temp[y]) - 97] += 1


print(amounts)
