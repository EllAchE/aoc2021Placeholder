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
    inputs.append([on, [int(cleaned[2]), int(cleaned[3])], [int(cleaned[5]), int(cleaned[6])], [int(cleaned[8]), int(cleaned[9])]])

# this is definitely going to have to change for whatever part 2 is
grid = {}
for input in inputs:
    on = input[0]
    x = input[1]
    y = input[2]
    z = input[3]

    skip = False

    if x[0] < -50:
        x[0] = -50
    if x[0] > 50:
        skip = True
    if x[1] < -50:
        skip = True
    if x[1] > 50:
        x[1] = 50
    if y[0] < -50:
        y[0] = -50
    if y[0] > 50:
        skip = True
    if y[1] < -50:
        skip = True
    if y[1] > 50:
        y[1] = 50
    if z[0] < -50:
        z[0] = -50
    if z[0] > 50:
        skip = True
    if z[1] < -50:
        skip = True
    if z[1] > 50:
        z[1] = 50

    if not skip:
        for i in range(x[0], x[1]+1):
            for j in range(y[0], y[1]+1):
                for k in range(z[0], z[1]+1):
                    if on:
                        grid[i,j,k] = on
                    elif (i,j,k) in grid:
                        grid.pop((i,j,k))
print len(grid)
