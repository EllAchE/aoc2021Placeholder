data = open("input.txt").readlines()
# copy the data to a list
lst = list(map(lambda a : int(a), data[0].split(',')))

def mapToDistanceCost(center, num):
    difference = abs(center - num)
    return (difference + 1) * difference / 2

def getSumOfGasCosts(center, arr):
    resArr = [mapToDistanceCost(center, a) for a in arr]
    return sum(resArr)

listLen = len(lst)
lst.sort()
lstCopy = lst.copy()
medianVal = lst
