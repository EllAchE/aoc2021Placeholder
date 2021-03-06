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
winningBoard = []
for d in drawOrder[4:]:
    if not solved:
        drawn.append(d)
        for board in boardWinPossiblities:
            for b in board:
                if set(b) <= set(drawn):
                    winningBoard = board
                    solved = True
                    break

lastCalled = int(drawn[-1])
winningBoard = winningBoard[:5]
winningBoard = [j for row in winningBoard for j in row] #flatten 2d array
for d in drawn:
    try:
        winningBoard.remove(d)
    except ValueError as e:
        continue

sum = 0
for w in winningBoard:
    sum += int(w)

print sum * lastCalled