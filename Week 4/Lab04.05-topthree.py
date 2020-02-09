#Program to keep reading students until user enters a blank string
#will assume it's a name even if numbers are entered, so take user input as str
import random
#take names from user
#to prevent case where space is used in place of blank, we strip the string so it is blank anyway
def generateRand(numOfNums, start, end):
    randomNumList=[]
    for i in range(numOfNums):
        randomNumList.append(random.randint(start,end))
    return randomNumList

randomList = generateRand(10,0,100)
print(randomList)
print(randomList.index(max(randomList)))
randomList.pop(randomList.index(max(randomList)))
#randomList.pop(randomList[max(randomList)])
#print(randomList)
print(randomList)

top3List =[]
top3List.append(randomList.pop(randomList.index(max(randomList))))
top3List.append(randomList.pop(randomList.index(max(randomList))))
top3List.append(randomList.pop(randomList.index(max(randomList))))
print(top3List)