data = open("input.txt", 'r')
grid = [list(map(int, d.strip())) for d in data]
data.close()

dist = []
for i in range(0, len(grid)):
    dist.append([-1] * len(grid[0]))

dist[0][0] = 0

def minDist(dist, spt):
    minDist = float("inf")
    minRow = 0
    minCol = 0

    for row in range(0, len(dist)):
        for col in range(0, len(dist[row])):
            if dist[row][col] != -1 and dist[row][col] < minDist and not spt[row][col]:
                minDist = dist[row][col]
                minRow = row
                minCol = col
    return minRow, minCol

def djikstra(grid, dist):
    spt = []
    for i in range(0, len(grid)):
        spt.append([False] * len(grid[0]))
    for row in range(0, len(grid)):
        for col in range(0, len(grid[row])):
            minRow, minCol = minDist(dist, spt)
            spt[minRow][minCol] = True
            if minRow == len(grid)-1 and minCol == len(grid[row])-1:
                return dist[minRow][minCol]

            if minRow > 0 and not spt[minRow-1][minCol]:
                if dist[minRow - 1][minCol] > -1:
                    dist[minRow - 1][minCol] = min(dist[minRow - 1][minCol], grid[minRow - 1][minCol] + dist[minRow][minCol])
                else:
                    dist[minRow - 1][minCol] = grid[minRow - 1][minCol] + dist[minRow][minCol]
            if minRow < len(grid) - 1 and not spt[minRow+1][minCol]:
                if dist[minRow + 1][minCol] > -1:
                    dist[minRow + 1][minCol] = min(dist[minRow + 1][minCol], grid[minRow + 1][minCol] + dist[minRow][minCol])
                else:
                    dist[minRow + 1][minCol] = grid[minRow + 1][minCol] + dist[minRow][minCol]
            if minCol > 0 and not spt[minRow][minCol-1]:
                if dist[minRow][minCol - 1] > -1:
                    dist[minRow][minCol-1] = min(dist[minRow][minCol-1],grid[minRow][minCol-1] + dist[minRow][minCol])
                else:
                    dist[minRow][minCol-1] = grid[minRow][minCol-1] + dist[minRow][minCol]
            if minCol < len(grid[minRow]) - 1 and not spt[minRow][minCol+1]:
                if dist[minRow][minCol+1] > -1:
                    dist[minRow][minCol+1] = min(dist[minRow][minCol+1], grid[minRow][minCol+1] + dist[minRow][minCol])
                else:
                    dist[minRow][minCol+1] = grid[minRow][minCol+1] + dist[minRow][minCol]

print djikstra(grid, dist)