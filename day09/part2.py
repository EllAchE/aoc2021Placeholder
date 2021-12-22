data = open("input.txt").readlines()
# copy the data to a list
lst = [list(d.strip()) for d in data] # split lines to arrays

lowList = []
for rowNum in range(0, len(lst)):
    for colNum in range(0, len(lst[0])):
        if rowNum != 0:
            if lst[rowNum - 1][colNum] <= lst[rowNum][colNum]:
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
        lowList.append([rowNum, colNum])

basins = [0,0,0]
for i in lowList:
    basinIncludes = [i]

    for b in basinIncludes:
        rowNum = b[0]
        colNum = b[1]
        if rowNum != 0 and not lst[rowNum - 1][colNum] == '9' and lst[rowNum - 1][colNum] > lst[rowNum][colNum]:
            if not [rowNum - 1, colNum] in basinIncludes:
                basinIncludes.append([rowNum - 1, colNum])
        if rowNum != len(lst) - 1 and not lst[rowNum + 1][colNum] == '9' and lst[rowNum + 1][colNum] > lst[rowNum][colNum]:
            if not [rowNum + 1, colNum] in basinIncludes:
                basinIncludes.append([rowNum + 1, colNum])
        if colNum != 0 and not lst[rowNum][colNum - 1] == '9' and lst[rowNum][colNum - 1] > lst[rowNum][colNum]:
            if not [rowNum, colNum - 1] in basinIncludes:
                basinIncludes.append([rowNum, colNum - 1])
        if colNum != len(lst[0]) - 1 and not lst[rowNum][colNum + 1] == '9' and lst[rowNum][colNum + 1] > lst[rowNum][colNum]:
            if not [rowNum, colNum + 1] in basinIncludes:
                basinIncludes.append([rowNum, colNum + 1])

    basins.sort()
    if len(basinIncludes) > basins[0]:
        basins[0] = len(basinIncludes)

ans = 1
for b in basins:
    ans *= b
print ans
