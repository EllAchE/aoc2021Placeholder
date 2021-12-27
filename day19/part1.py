data = open("input.txt").readlines()
# copy the data to a list
lst = [d.strip() for d in data]

# this is a really messy input parser sorry
scanNum = 0
scanners = [[]]
for l in lst:
    if 'scanner' in l:
        scanners[scanNum] = [i for i in scanners[scanNum] if i != []]
        scanners.append([])
        scanNum += 1
    else:
        line = [i for i in l.split(',')]
        line = filter(None, line)
        line = [int(i) for i in line]
        scanners[scanNum].append(line)
scanners = scanners[1:]


def shuffle(coordinates, rotate):
    for i in range(0, rotate):
        coordinates.append(coordinates.pop(0))


def match(baseline, add):
    origin = [(1,1,1), (1,1,-1), (1,-1,1), (1,-1,-1), (-1,1,1), (-1,1,-1), (-1,-1,1), (-1,-1,-1)]
    axes = [()]
    for x,y,z in origin:
        for flip in range(2):
            for shuffleAxis in range(0, 3):
                matched = {}
                addCopy = [[i for i in row] for row in add]
                for a in addCopy:
                    if flip == 0:
                        # xyz, zxy, yzx
                        shuffle(a, shuffleAxis)
                    else:
                        # xzy, zyx, yxz
                        shuffle(a, shuffleAxis)
                        a.reverse()
                    a[0] = a[0] * x
                    a[1] = a[1] * y
                    a[2] = a[2] * z
                    for b in baseline:
                        delta = tuple([b_i - a_i for a_i, b_i in zip(a, b)])
                        if delta in matched:
                            matched[delta] += 1
                        else:
                            matched[delta] = 1
                        if matched[delta] >= 12:
                            return delta, x,y,z, shuffleAxis, flip
    return None, None, None, None, None, None


baseline = scanners.pop(0)
offset = [0, 0, 0]
while len(scanners) > 0:
    scanner = scanners.pop(0)
    scannerCopy = [[i for i in row] for row in scanner]
    offset, x_direction, y_direction, z_direction, shuffleAxis, flip = match(baseline, scannerCopy)
    # print 'params', offset, x_direction, y_direction, z_direction, shuffleAxis
    if offset is not None:

        for i in scanner:
            if flip == 0:
                shuffle(i, shuffleAxis)
            else:
                shuffle(i, shuffleAxis)
                i.reverse()
            i[0] = i[0] * x_direction
            i[1] = i[1] * y_direction
            i[2] = i[2] * z_direction
            i = [a_i + o for a_i, o in zip(i, offset)]
            if i not in baseline:
                baseline.append(i)
    else:
        scanners.append(scanner)

# baseline.sort()
# print baseline
print len(baseline)