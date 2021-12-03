data = open("input.txt").readlines()
# copy the data to a list
lst = [d.strip() for d in data]

def countIncreases():
    intlst = list(map(lambda a: int(a), lst))
    total = 0

    oldSum = sum(intlst[:3])
    print(oldSum)
    for i in range(1, len(intlst) - 2):
        newSum = sum(intlst[i:i+3])
        if newSum > oldSum:
            total += 1
        print("total {} oldItem {} Item {}".format(total, oldSum, newSum))
        oldSum = newSum
    return total


print(countIncreases())