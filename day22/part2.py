import re

data = open("input.txt").readlines()
# copy the data to a list
lst = [d.strip() for d in data]
inputs = []

for l in lst:
    cleaned = re.split(',|\.\.|.=| |', l)
    on = False
    if cleaned[0] == 'on':
        on = True
    inputs.append([on, ([int(cleaned[2]), int(cleaned[3])], [int(cleaned[5]), int(cleaned[6])], [int(cleaned[8]), int(cleaned[9])])])

# (done with a lot of online help)
ranges = []
for inp in inputs:
    print inp
    on = inp[0]
    ix, iy, iz = inp[1]
    iterate = len(ranges)
    for r in range(iterate):
        rx, ry, rz = ranges[r]

        # no overlap
        if ix[0] > rx[1] or ix[1] < rx[0] or iy[0] > ry[1] or iy[1] < ry[0] or iz[0] > rz[1] or iz[1] < rz[0]:
            continue

        # if there is an overlap, split off the non input cube ranges
        ranges[r] = None
        # pad/skim coordinates by 1 since the edge row of cubes is counted as part of the input
        if ix[0] > rx[0]: # bottom of input higher than bottom of existing
            ranges.append(([rx[0], ix[0]-1], ry, rz))
        if ix[1] < rx[1]: # top of input lower than top of existing
            ranges.append(([ix[1]+1, rx[1]], ry, rz))
        if iy[0] > ry[0]:
            ranges.append(([max(ix[0], rx[0]), min(ix[1], rx[1])], [ry[0], iy[0]-1], rz))
        if iy[1] < ry[1]:
            ranges.append(([max(ix[0], rx[0]), min(ix[1], rx[1])], [iy[1]+1, ry[1]], rz))
        if iz[0] > rz[0]:
            ranges.append(([max(ix[0], rx[0]), min(ix[1], rx[1])], [max(iy[0], ry[0]), min(iy[1], ry[1])], [rz[0], iz[0]-1]))
        if iz[1] < rz[1]:
            ranges.append(([max(ix[0], rx[0]), min(ix[1], rx[1])], [max(iy[0], ry[0]), min(iy[1], ry[1])], [iz[1]+1, rz[1]]))
    # add in the entire input cube
    if on:
        ranges.append((ix, iy, iz))
    ranges = [r for r in ranges if r is not None]

total = 0
for rangeX, rangeY, rangeZ in ranges:
    total += (abs(rangeX[0]-rangeX[1])+1) * (abs(rangeY[0]-rangeY[1])+1) * (abs(rangeZ[0]-rangeZ[1])+1)
print total
