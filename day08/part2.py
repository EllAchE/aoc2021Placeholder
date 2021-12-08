data = open("input.txt").readlines()
# copy the data to a list
lst = [d.strip() for d in data]

def splitInputAndOutput(line):
    ioLine = line.split(' | ')
    return {
        "input": ioLine[0].split(),
        "output": ioLine[1].split()
    }

formattedLst = list(map(splitInputAndOutput, lst))

# Deductive logic
# 1,4,7,8 known by default
# 5 can be identified by single pt difference; it's the only one sharing all but one thing with both 6 & 9
# then 3 and 9 can be found, also finding 6
# now 1,3,4,5,6,7,8,9
# with 6 & 9 known, 0 can also be found, and with 5 and 3 you can find 2

# 2 can also be IDed with the bottom left segment and 3 is the only one left

def createNumLetterMap(tenNumbersSet):
    numLetterMap = {}
    tempMap = {
        5: [],
        6: []
    }

    for item in tenNumbersSet:
        if len(item) == 2:
            numLetterMap[item] = 1
        elif len(item) == 3:
            numLetterMap[item] = 7
        elif len(item) == 4:
            numLetterMap[item] = 4
        elif len(item) == 7:
            numLetterMap[item] = 8
        elif len(item) == 5:
            tempMap[5].append(set(item.split())) # should turn into char array
        elif len(item) == 6:
            tempMap[6].append(set(item.split())) # should turn into char array

    def findFive(tempMap):
        for charSetOf5 in tempMap[5]:
            totalSubsets = 0
            for charSetOf6 in tempMap[6]:
                if charSetOf5.issubset(charSetOf6):
                    totalSubsets += 1
                    if totalSubsets == 2:
                        return charSetOf5

    def findThreeAndNine(tempMap): # Requires 5 to be known and removed
        for charSetOf5 in tempMap[5]:
            for charSetOf6 in tempMap[6]:
                if charSetOf5.issubset(charSetOf6):
                    return charSetOf5, charSetOf6

    def findSix(fiveStringSet, tempMap): # Requires above to be known and removed
        for charSetOf6 in tempMap[6]:
            if fiveStringSet.issubset(charSetOf6):
                    return charSetOf6




total = 0
outputSet = set()
for line in formattedLst:
    for item in line["output"]:
        if len(item) == 2 or len(item) == 4 or len(item) == 3 or len(item) == 7:
            total += 1
            outputSet.add(item)

