data = open("input.txt").readlines()
# copy the data to a list
lst = [d.strip() for d in data]
convertedInput = list(map(lambda a : list(a), lst))

# cols = 10, rows = 9

#################
# SOLUTION
#################
# I will be manually calculating each step. I'll maintain a list of cucumber objects and for each "step" I'll check if
# they can move or not. The east and south steps can be considered separately, but 2 must occur for a counted step.
# This will iterate until an east and south step both occur with no movement, which means no further steps will occur.
# looking at cycles of the different cucumber rows could have a more elegant soln.

def createCucumberIndexList(convertedInput):
    cIndexLst = []
    for i in range(0, len(convertedInput)):
        for j in range(0, len(convertedInput[0])):
            if convertedInput[i][j] != ".":
                if convertedInput[i][j] == ">":
                    cIndexLst.append({"x": j, "y": i, "type": "east", "canmove": False})
                elif convertedInput[i][j] == "v":
                    cIndexLst.append({"x": j, "y": i, "type": "south", "canmove": False})
                else:
                    raise AttributeError

    return cIndexLst

def cucumberStep(cMap, cucumberIndexListIn):
    anyMove = False
    eastList = list(filter(lambda a: a["type"] == "east", cucumberIndexListIn))
    southList = list(filter(lambda a: a["type"] == "south", cucumberIndexListIn))
    for cucumber in eastList:
        checkIfCanMoveEast(cucumber, cMap)
    for cucumber in eastList:
        if cucumber["canmove"]:
            moveEast(cucumber, cMap)
            anyMove = True

    for cucumber in southList:
        checkIfCanMoveSouth(cucumber, cMap)
    for cucumber in southList:
        if cucumber["canmove"]:
            moveSouth(cucumber, cMap)
            anyMove = True

    return anyMove # flipped my booleans...

def checkIfCanMoveEast(cucumber, cMap):
    if cucumber["x"] == 9: # map edge
        if cMap[cucumber["y"]][0] == ".":
            cucumber["canmove"] = True
        else:
            cucumber["canmove"] = False
    else:
        if cMap[cucumber["y"]][cucumber["x"] + 1] == ".":
            cucumber["canmove"] = True
        else:
            cucumber["canmove"] = False

def checkIfCanMoveSouth(cucumber, cMap):
    if cucumber["y"] == 8: # map edge
        if cMap[0][cucumber["x"]] == ".":
            cucumber["canmove"] = True
        else:
            cucumber["canmove"] = False
    else:
        if cMap[cucumber["y"] + 1][cucumber["x"]] == ".":
            cucumber["canmove"] = True
        else:
            cucumber["canmove"] = False

def moveEast(cucumber, cMap):
    cMap[cucumber["y"]][cucumber["x"]] = "."
    cucumber["x"] = (cucumber["x"] + 1) % 10
    cMap[cucumber["y"]][cucumber["x"]] = ">"
    cucumber["canmove"] = False

def moveSouth(cucumber, cMap):
    cMap[cucumber["y"]][cucumber["x"]] = "."
    cucumber["y"] = (cucumber["y"] + 1) % 9
    cMap[cucumber["y"]][cucumber["x"]] = "v"
    cucumber["canmove"] = False


cucumberIndexList = createCucumberIndexList(convertedInput)
isNotStuck = True
stepCount = 0
while isNotStuck: # does assume at least 1 step
    print(cucumberIndexList)
    isNotStuck = cucumberStep(convertedInput, cucumberIndexList)
    print(cucumberIndexList)
    stepCount += 1

print(stepCount)