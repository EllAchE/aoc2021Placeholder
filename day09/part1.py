data = open("input.txt").readlines()
# copy the data to a list
lst = [list(d.strip()) for d in data] # split lines to arrays

print(lst)

lowList = []
for rowNum in range(0, len(lst)):
    for colNum in range(0, len(lst[0])):
        #isLow = True
        if rowNum != 0:
            if lst[rowNum - 1][colNum] <= lst[rowNum][colNum]:
                #isLow = False
                continue
        if rowNum != len(lst) - 1:
            if lst[rowNum + 1][colNum] <= lst[rowNum][colNum]:
                continue
        if colNum != 0:
            if lst[rowNum][colNum - 1] <= lst[rowNum][colNum]:
                continue
        if colNum != len(lst[0]) - 1:
            if lst[rowNum][colNum + 1] <= lst[rowNum][colNum]:
                continue
        lowList.append(lst[rowNum][colNum])

print(lowList)
intLowList = list(map(lambda a : int(a), lowList))
print(sum(intLowList) + len(lowList)) # add 1 to all
