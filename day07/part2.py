data = open("input.txt").readlines()
# copy the data to a list
lst = list(map(lambda a : int(a), data[0].split(',')))

def getMedian(lstCopy):
    if len(lstCopy) % 2 == 0:
        medianVal = (lstCopy[len(lstCopy)//2] + lstCopy[len(lstCopy)//2-1]) / 2 # assumes list has min length of 2
    else:
        medianVal = lstCopy[len(lstCopy)//2]
    return medianVal

def mapToDistanceCost(center, num):
    difference = abs(center - num)
    return (difference + 1) * difference / 2

def getSumOfGasCosts(center, arr):
    resArr = [mapToDistanceCost(center, a) for a in arr]
    return sum(resArr)

lst.sort()
lstCopy = lst.copy()
isMinimumCost = False
center = getMedian(lstCopy)
currCost = getSumOfGasCosts(center, lstCopy)
print("og median", center)

while not isMinimumCost:
    rightCost = getSumOfGasCosts(center + 1, lstCopy)
    leftCost = getSumOfGasCosts(center - 1, lstCopy)
    if rightCost < currCost:
        currCost = rightCost
        center += 1
    elif leftCost < currCost:
        currCost = leftCost
        center -= 1
    else:
        isMinimumCost = True

print(lstCopy)
print(center)
print(currCost)