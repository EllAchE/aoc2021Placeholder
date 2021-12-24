# Just going to hard code in the target area
targetX = [81, 129]
targetY = [-150, -108]

# targetX = [20, 30]
# targetY = [-10, -5]

def inTarget(x, y):
    return x >= targetX[0] and x <= targetX[1] and y >= targetY[0] and y <= targetY[1]


maxHeight = 0
# for the whole upwards parabola it takes abs(targetY[0]) steps to reach the peak and and the same to return to 0,0
for steps in range(1, 2*abs(targetY[0])+1):
    minVx = 0
    maxVx = 1000

    # vy on the way down at y=0 is same as initial vy0
    minVy = 0
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

                peak = (vy * (vy+1))/2
                if peak > maxHeight:
                    maxHeight = peak
                    # print peak



print maxHeight