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
        if len(item) == 5:
            tempMap[5].append({"og": item, "setVals": set(item)}) # should turn into char array
        elif len(item) == 6:
            tempMap[6].append({"og": item, "setVals": set(item)}) # should turn into char array

    def findFive(tempMap):
        for charSetOf5 in tempMap[5]:
            totalSubsets = 0
            for charSetOf6 in tempMap[6]:
                if charSetOf5["setVals"].issubset(charSetOf6["setVals"]):
                    totalSubsets += 1
                    if totalSubsets == 2:
                        return charSetOf5

    def findThreeAndNine(tempMap): # Requires 5 to be known and removed
        for charSetOf5 in tempMap[5]:
            for charSetOf6 in tempMap[6]:
                if charSetOf5["setVals"].issubset(charSetOf6["setVals"]):
                    return charSetOf5, charSetOf6

    def findSix(fiveStringSet, tempMap): # Requires above to be known and removed
        for charSetOf6 in tempMap[6]:
            if fiveStringSet["setVals"].issubset(charSetOf6["setVals"]):
                return charSetOf6

    fiveSet = findFive(tempMap)
    tempMap[5].remove(fiveSet)
    threeSet, nineSet = findThreeAndNine(tempMap)
    tempMap[5].remove(threeSet)
    tempMap[6].remove(nineSet)
    sixSet = findSix(fiveSet, tempMap)
    tempMap[6].remove(sixSet)
    zeroSet = tempMap[6].pop()
    twoSet = tempMap[5].pop()
    # now has objects for all values which include a set and the original

    numLetterMap["".join(sorted(fiveSet["setVals"]))] = 5
    numLetterMap["".join(sorted(threeSet["setVals"]))] = 3
    numLetterMap["".join(sorted(nineSet["setVals"]))] = 9
    numLetterMap["".join(sorted(sixSet["setVals"]))] = 6
    numLetterMap["".join(sorted(zeroSet["setVals"]))] = 0
    numLetterMap["".join(sorted(twoSet["setVals"]))] = 2

    return numLetterMap


total = 0
for line in formattedLst:
    numLetterMap = createNumLetterMap(line["input"])
    multiplier = 1000
    for item in line["output"]:
        compareItem = "".join(sorted(item))
        if len(item) == 2:
            total += 1 * multiplier
        elif len(item) == 3:
            total += 7 * multiplier
        elif len(item) == 4:
            total += 4 * multiplier
        elif len(item) == 7:
            total += 8 * multiplier
        else:
            total += multiplier * numLetterMap[compareItem] # All works except that the outputs aren't ordered consistently
        multiplier /= 10

print(total)
