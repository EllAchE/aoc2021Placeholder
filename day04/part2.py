data = open("input.txt", 'r')
drawOrder = data.readline().strip().split(",")
data.close()

data = open("input.txt").readlines()
lst = [d.strip() for d in data[2:]]

def extractCol(lst, colNum):
    return [row[colNum] for row in lst]

boardNum = 0
boardWinPossiblities = [[]]
for line in lst:
    if line:
        boardWinPossiblities[boardNum].append(line.strip().split())
    else:
        board = []
        boardWinPossiblities.append(board)
        boardNum += 1
for board in boardWinPossiblities:
    numRows = len(board)
    numCols = len(board[0])
    for i in range(0, numCols):
        board.append(extractCol(board[0:numRows], i))

solved = False
drawn = drawOrder[0:4]
winningBoards = []
lastCalled = -1
finalDrawn = []
for d in drawOrder[4:]:
    drawn.append(d)
    for boardNum in range(0,len(boardWinPossiblities)):
        for b in boardWinPossiblities[boardNum]:
            if set(b) <= set(drawn) and winningBoards.count(boardNum) == 0:
                winningBoards.append(boardNum)
                if len(winningBoards) == len(boardWinPossiblities) and lastCalled == -1:
                    lastCalled = int(d)
                    finalDrawn = drawn[:]

lastWinner = winningBoards[-1]
lastWinningBoard = boardWinPossiblities[lastWinner][:5]
lastWinningBoard = [j for row in lastWinningBoard for j in row]  #flatten 2d array
for d in finalDrawn:
    try:
        lastWinningBoard.remove(d)
    except ValueError as e:
        continue

sum = 0
print finalDrawn
for w in lastWinningBoard:
    sum += int(w)

print sum * lastCalled