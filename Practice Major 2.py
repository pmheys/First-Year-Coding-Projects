inFile = open("inputFile.txt", "r")

data = inFile.read()
top = 0
bot = 0
tempList = []

tempList = data.split('\n')
finalList = []

for i in range(len(tempList)):
    subList = tempList[i].split(',')
    top += float(subList[0])*float(subList[1])
    bot += float(subList[1])
    finalList.append(subList)

inFile.close()
outFile = open("hiPaul.txt", "w")
outFile.write("hola")
outFile.close()





