# Just going to hard code in the target area
targetX = [81, 129]
targetY = [-150, -108]

# targetX = [20, 30]
# targetY = [-10, -5]


def inTarget(x, y):
    return x >= targetX[0] and x <= targetX[1] and y >= targetY[0] and y <= targetY[1]


count = set()
#semi brute forcing this
for steps in range(1, 2*abs(targetY[0])+1):
    minVx = -abs(targetX[0])
    maxVx = targetX[1]+1

    # vy on the way down at y=0 is same as initial vy0
    minVy = targetY[0]
    maxVy = abs(targetY[0])

    for vx in range(minVx, maxVx):
        finalX = 0
        for s in range(1, steps+1):
            if finalX < vx*s - ((s*(s-1))/2):
                finalX = vx*s - ((s*(s-1))/2)
        for vy in range(minVy, maxVy):
            finalY = vy*steps - ((steps*(steps-1))/2)

            if inTarget(finalX, finalY):
                # print '(vx, vy): ', vx, vy, '(finalX, finalY): ', finalX, finalY, 'steps: ', steps
                count.add((vx, vy))

print len(count)
