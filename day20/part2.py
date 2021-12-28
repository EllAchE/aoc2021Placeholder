data = open("input.txt", 'r')
enhance = data.readline()
data.close()

data = open("input.txt").readlines()

enhanceBits = set()
for i, c in enumerate(enhance):
    if c == '#':
        enhanceBits.add(i)

inputBits = []
gridSize = [len(data[2:]),len(data[2])]
for rowNum, line in enumerate(data[2:]):
    rowBits = []
    for colNum, c in enumerate(line):
        if c == '#':
            rowBits.append(colNum)
    inputBits.append(rowBits)

# print enhanceBits
# print inputBits

# enhancing twice, 0 and 512 in enhancement string flips all the infinite dark pixels back to original

def getSurrounding(row, col, inputBits, light):
    # print row, col
    binary = ''
    if row > 0 and len(inputBits[row-1]) >= 1:
        # print 'top', inputBits[row-1]
        if not 0 <= col - 1 <= gridSize[1]:
            binary += str(light)
        elif col - 1 in inputBits[row-1]:
            binary += '1'
        else:
            binary += '0'
        if not 0 <= col <= gridSize[1]:
            binary += str(light)
        elif col in inputBits[row-1]:
            binary += '1'
        else:
            binary += '0'
        if not 0 <= col + 1 <= gridSize[1]:
            binary += str(light)
        elif col+1 in inputBits[row-1]:
            binary += '1'
        else:
            binary += '0'
    else:
        binary += str(light)*3

    if 0 <= row <= len(inputBits)-1 and len(inputBits[row]) >= 1:
        # print 'mid', inputBits[row]
        if not 0 <= col - 1 <= gridSize[1]:
            binary += str(light)
        elif col - 1 in inputBits[row]:
            binary += '1'
        else:
            binary += '0'
        if not 0 <= col <= gridSize[1]:
            binary += str(light)
        elif col in inputBits[row]:
            binary += '1'
        else:
            binary += '0'
        if not 0 <= col + 1 <= gridSize[1]:
            binary += str(light)
        elif col + 1 in inputBits[row]:
            binary += '1'
        else:
            binary += '0'
    else:
        binary += str(light)*3

    if row < len(inputBits)-1 and len(inputBits[row+1]) >= 1:
        # print 'bot', inputBits[row+1]
        if not 0 <= col - 1 <= gridSize[1]:
            binary += str(light)
        elif col - 1 in inputBits[row+1]:
            binary += '1'
        else:
            binary += '0'
        if not 0 <= col <= gridSize[1]:
            binary += str(light)
        elif col in inputBits[row+1]:
            binary += '1'
        else:
            binary += '0'
        if not 0 <= col + 1 <= gridSize[1]:
            binary += str(light)
        elif col+1 in inputBits[row+1]:
            binary += '1'
        else:
            binary += '0'
    else:
        binary += str(light)*3

    # print binary
    return int(binary, 2)


def getEnhance(inputNum, enhanceBits):
    if inputNum in enhanceBits:
        return True
    return False


for iterate in range(0,50):
    #buffer lines
    inputBits.insert(0, [])
    inputBits.append([])
    # print inputBits

    newInput = []
    for i in range(-1, gridSize[0]+2):
        newInput.append([])
        for j in range(-1, gridSize[1]+2):
            if getEnhance(getSurrounding(i, j, inputBits, iterate%2), enhanceBits):
                newInput[i+1].append(j+1)

    # print newInput
    inputBits = newInput[1:]
    gridSize = [gridSize[0]+2, gridSize[1]+2]

lit = 0
for i in inputBits:
    lit += len(i)
print lit
