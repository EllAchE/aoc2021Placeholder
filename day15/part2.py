import heapq

data = open("input.txt", 'r')
grid = [list(map(int, d.strip())) for d in data]
data.close()

for row in range(0, len(grid)):
    newRow = []
    for add in range(1, 5):
        newRow += [9 if (i + add) % 9 == 0 else (i + add) % 9 for i in grid[row]]
    grid[row] = grid[row] + newRow

newBlock = []
for add in range(1, 5):
    for row in range(0, len(grid)):
        newRow = [9 if (i + add) % 9 == 0 else (i + add) % 9 for i in grid[row]]
        newBlock.append(newRow)
grid += newBlock


dist = []
for i in range(0, len(grid)):
    dist.append([-1] * len(grid[0]))

dist[0][0] = 0

def djikstra(grid, dist):
    spt = []
    candidates = [(0, [0, 0])]

    for i in range(0, len(grid)):
        spt.append([False] * len(grid[0]))
    for row in range(0, len(grid)):
        for col in range(0, len(grid[row])):
            distance, coordinates = heapq.heappop(candidates)
            minRow, minCol = coordinates[0], coordinates[1]
            spt[minRow][minCol] = True

            if minRow == len(grid)-1 and minCol == len(grid[row])-1:
                return dist[minRow][minCol]

            if minRow > 0 and not spt[minRow-1][minCol]:
                if dist[minRow - 1][minCol] > -1:
                    if dist[minRow - 1][minCol] > grid[minRow - 1][minCol] + dist[minRow][minCol]:
                        dist[minRow - 1][minCol] = grid[minRow - 1][minCol] + dist[minRow][minCol]
                        heapq.heappush(candidates, (dist[minRow - 1][minCol], [minRow - 1, minCol]))
                else:
                    dist[minRow - 1][minCol] = grid[minRow - 1][minCol] + dist[minRow][minCol]
                    heapq.heappush(candidates, (dist[minRow - 1][minCol], [minRow - 1, minCol]))
            if minRow < len(grid) - 1 and not spt[minRow+1][minCol]:
                if dist[minRow + 1][minCol] > -1:
                    if dist[minRow + 1][minCol] > grid[minRow + 1][minCol] + dist[minRow][minCol]:
                        dist[minRow + 1][minCol] = grid[minRow + 1][minCol] + dist[minRow][minCol]
                        heapq.heappush(candidates, (dist[minRow + 1][minCol], [minRow + 1, minCol]))
                else:
                    dist[minRow + 1][minCol] = grid[minRow + 1][minCol] + dist[minRow][minCol]
                    heapq.heappush(candidates, (dist[minRow + 1][minCol], [minRow + 1, minCol]))
            if minCol > 0 and not spt[minRow][minCol-1]:
                if dist[minRow][minCol - 1] > -1:
                    if dist[minRow][minCol-1] > grid[minRow][minCol-1] + dist[minRow][minCol]:
                        dist[minRow][minCol - 1] = grid[minRow][minCol-1] + dist[minRow][minCol]
                        heapq.heappush(candidates, (dist[minRow][minCol - 1], [minRow, minCol-1]))
                else:
                    dist[minRow][minCol - 1] = grid[minRow][minCol-1] + dist[minRow][minCol]
                    heapq.heappush(candidates, (dist[minRow][minCol - 1], [minRow, minCol - 1]))
            if minCol < len(grid[minRow]) - 1 and not spt[minRow][minCol+1]:
                if dist[minRow][minCol+1] > -1:
                    if dist[minRow][minCol+1] > grid[minRow][minCol+1] + dist[minRow][minCol]:
                        dist[minRow][minCol+1] = grid[minRow][minCol+1] + dist[minRow][minCol]
                        heapq.heappush(candidates, (dist[minRow][minCol+1], [minRow, minCol+1]))
                else:
                    dist[minRow][minCol+1] = grid[minRow][minCol+1] + dist[minRow][minCol]
                    heapq.heappush(candidates, (dist[minRow][minCol+1], [minRow, minCol + 1]))

print djikstra(grid, dist)