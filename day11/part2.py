data = open("input.txt").readlines()
# copy the data to a list
lst = [d.strip() for d in data]

# x,y = 0,0 starting at top left
def flash(grid, x, y):
    if x > 0:
        # left
        grid[x - 1][y] = grid[x - 1][y] + 1
        if grid[x - 1][y] == 10:
            flash(grid, x - 1, y)
        # top left
        if y > 0:
            grid[x - 1][y - 1] = grid[x - 1][y - 1] + 1
            if grid[x - 1][y - 1] == 10:
                flash(grid, x - 1, y - 1)
        # bottom left
        if y < 9:
            grid[x - 1][y + 1] = grid[x - 1][y + 1] + 1
            if grid[x - 1][y + 1] == 10:
                flash(grid, x - 1, y + 1)
    if x < 9:
        # right
        grid[x + 1][y] = grid[x + 1][y] + 1
        if grid[x + 1][y] == 10:
            flash(grid, x + 1, y)
        # top right
        if y > 0:
            grid[x + 1][y - 1] = grid[x + 1][y - 1] + 1
            if grid[x + 1][y - 1] == 10:
                flash(grid, x + 1, y - 1)
        # bottom right
        if y < 9:
            grid[x + 1][y + 1] = grid[x + 1][y + 1] + 1
            if grid[x + 1][y + 1] == 10:
                flash(grid, x + 1, y + 1)
    # above
    if y > 0:
        grid[x][y - 1] = grid[x][y - 1] + 1
        if grid[x][y - 1] == 10:
            flash(grid, x, y - 1)
    # below
    if y < 9:
        grid[x][y + 1] = grid[x][y + 1] + 1
        if grid[x][y + 1] == 10:
            flash(grid, x, y + 1)


grid = []
for l in lst:
    line = [int(i) for i in list(l)]
    grid.append(line)

sync = False
step = 1
while not sync:
    for y in range(0, 10):
        for x in range(0, 10):
            grid[x][y] = grid[x][y] + 1
            if grid[x][y] == 10:
                flash(grid, x, y)

    stepSync = True
    for y in range(0, 10):
        for x in range(0, 10):
            if grid[x][y] > 9:
                grid[x][y] = 0
            else:
                stepSync = False

    if stepSync:
        break
    else:
        step = step + 1

print step
