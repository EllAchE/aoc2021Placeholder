data = open("input.txt").readlines()
# copy the data to a list
lst = [d.strip() for d in data]
convertedInput = list(map(lambda a : list(a), lst))

# cols = 10, rows = 9
# cIndex will include ["x pos", y pos, type]

cMap = []
cIndexLst = []

#################
# SOLUTION
#################

# I will be manually calculating each step. I'll maintain a list of cucumber objects and for each "step" I'll check if
# they can move or not. The east and south steps can be considered separately, but 2 must occur for a counted step.
# This will iterate until an east and south step both occur with no movement, which would mean no further steps will occur.
# looking at cycles of the different cucumber rows could have a more elegant soln.

def createMapAndList(lst):
    for inRow in lst:
        for item in inRow:


def checkIndexList():
    anyMove = False
    for cucumber in lst:
        checkSpot(cucumber, cMap)

def checkIfCanMoveEast(cucumber, cMap):
    if cucumber["x"] == 9: # map edge
        if cMap[cucumber["y"]][0] == ".":
            cucumber["canmove"] = True
        else:
            cucumber["canmove"] = False
    else:
        if cMap[cucumber["y"]][cucumber["x"]+1] == ".":
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

def checkSpot(cucumber, cMap):
    if cucumber["type"] == "east":
        checkIfCanMoveEast(cucumber, cMap)
    elif cucumber["type"] == "south":
        checkIfCanMoveSouth(cucumber, cMap)
