import math

data = open("input.txt").readlines()
# copy the data to a list
lst = list(map(lambda a : int(a), data[0].split(',')))
#lst = [16,1,2,0,4,2,7,1,2,14]

import numpy as np

def mapToAbsVal(num):
    return abs(num - 343)

# 343 - 340987
# 344 - 340989
# 342 - 340989
print(lst)
listLen = len(lst)
lst.sort()
medianVal = np.median(lst)

print(medianVal)
print(lst)
print(lst[listLen//2])

absList = list(map(mapToAbsVal, lst))

print(sum(absList))
