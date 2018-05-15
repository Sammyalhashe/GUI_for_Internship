def getBiggestRegion(grid):
    maxRegion = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            maxRegion = max(maxRegion, countCells(grid, i, j))
    return maxRegion


def countCells(grid, i, j):
    if (not(i in range(len(grid)) and j in range(len(grid[0])))):
        return 0
    if (grid[i][j] == 0):
        return 0
    count = 1
    grid[i][j] = 0
    count += countCells(grid, i + 1, j)
    count += countCells(grid, i - 1, j)
    count += countCells(grid, i, j + 1)
    count += countCells(grid, i, j - 1)
    count += countCells(grid, i + 1, j + 1)
    count += countCells(grid, i - 1, j - 1)
    count += countCells(grid, i - 1, j + 1)
    count += countCells(grid, i + 1, j - 1)
    return count


n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)


print(getBiggestRegion(grid))
