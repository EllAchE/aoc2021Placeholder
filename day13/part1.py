data = open("input.txt").readlines()
# copy the data to a list
lst = [d.strip() for d in data]

holes = []
folds = []
for l in lst:
    line = l.split(',')
    if len(line) > 1:
        line[0] = int(line[0])
        line[1] = int(line[1])
        holes.append(line)
    else:
        fold = line[0].split("fold along ")
        if len(fold) > 1:
            fold = fold[1]
            fold = fold.split('=')
            fold[1] = int(fold[1])
            folds.append(fold)
print holes
print folds

for fold in folds[:1]:
    axis = 0
    if fold[0] == 'y':
        axis = 1

    originalHoles = holes[:]
    for hole in holes:
        if hole[axis] > fold[1]:
            originalHoles.remove(hole)
            hole[axis] = abs(hole[axis] - (2*fold[1]))
            if hole in originalHoles:
                originalHoles.remove(hole)
            originalHoles.append(hole)
    holes = originalHoles[:]

holes.sort()
print holes
print len(holes)