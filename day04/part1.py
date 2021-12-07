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

# Maybe use sets here to check solutions against a subset of drawn numbers?

