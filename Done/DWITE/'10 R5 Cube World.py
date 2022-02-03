def waterCapacity(height, unusable, heights):
    for i in range(len(heights)):
        for j in range(len(heights[0])):
            
            unusable[i][j] = heights[i][j] > height

    for i in range(len(heights)):
        for j in range(len(heights[0])):
            if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
                floodFill(unusable, i, j)


    counter = 0
    for i in range(rows):
        for j in range(cols):
            if not unusable[i][j]:
                counter += 1

    return counter


def floodFill(grid, i, j):
    if i < 0 or i >= rows or j < 0 or j >= cols:
        return
    if (grid[i][j]):
        return
    grid[i][j] = True
    floodFill(grid, i, j - 1)
    floodFill(grid, i, j + 1)
    floodFill(grid, i - 1, j)
    floodFill(grid, i + 1, j)

for _ in range(5):
    rows, cols = [int(x) for x in input().split(' ')]


    heights = [[int(x) for x in input().split(' ')] for _ in range(rows)]
    print(heights)
    if rows <= 2 or cols <= 2:
        print(0)
    else:
        water = 0
        for i in range(51):
            water += waterCapacity(i, [[False for _ in range(len(heights[0]))] for _ in range(rows)], heights)

        print(water)