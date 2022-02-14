# height, width, dist = map(int, input().split())

# grid = [[int(x) for x in input().split()] for _ in range(height)]
# secondGrid = [x.copy() for x in grid]

# for h in range(height):
#     for w in range(width):
#         smallest = 1000000000
#         found = False
#         if grid[h][w] != 0:
#             continue
#         for x in range(dist):
#             if h-(x+1) >= 0 and grid[h-(x+1)][w] != 0:
#                 smallest = min(smallest, grid[h-(x+1)][w])
#                 found = True
#                 print(h, w, 1)
#             if h+(x+1) < height and grid[h+(x+1)][w] != 0:
#                 smallest = min(smallest, grid[h+(x+1)][w])
#                 found = True
#                 print(h, w, 2)
#             if w-(x+1) >= 0 and grid[h][w-(x+1)] != 0:
#                 smallest = min(smallest, grid[h][w-(x+1)])
#                 print(h, w, 3)
#                 print(smallest)
#                 found = True   
#             if w+(x+1) < width and grid[h][w+(x+1)] != 0:
#                 smallest = min(smallest, grid[h][w+(x+1)])
#                 found = True 
#                 print(h, w, 4)
#             if found:
#                 secondGrid[h][w] = smallest
#                 break

# for h in range(height):
#     for w in range(width-1):
#         print(secondGrid[h][w], end=' ')
#     print(secondGrid[h][width-1])





# height, width, maxDist = map(int, input().split())

# grid = [[int(x) for x in input().split()] for _ in range(height)]
# secondGrid = [x.copy() for x in grid]

# def ifValid(h, w, maxDist, dist):
#     found = False
#     smallest = 1000000000
#     if h >= height or h < 0 or w >= width or w < 0:
#         return
    
#     if h-1 >= 0 and grid[h-1][w] != 0:
#         smallest = min(smallest, grid[h-1][w])
#         found = True

#     if h+1 < height and grid[h+1][w] != 0:
#         smallest = min(smallest, grid[h+1][w])
#         found = True

#     if w-1 >= 0 and grid[h][w-1] != 0:
#         smallest = min(smallest, grid[h][w-1])

#         found = True   

#     if w+1 < width and grid[h][w+1] != 0:
#         smallest = min(smallest, grid[h][w+1])
#         found = True

#     if found:
#         return smallest
#     elif dist < maxDist:
#         smallestColour = (min(ifValid(h-1, w, maxDist, dist+1), ifValid(h+1, w, maxDist, dist+1), ifValid(h, w-1, maxDist, dist+1), ifValid(h, w+1, maxDist, dist+1)))
#     else:
#         return 69696969696

# for y in range(height):
#     for x in range(width):
#         if grid[y][x] != 0:
#             continue
#         secondGrid[y][x] = ifValid(y, x, maxDist, 1)

# for h in range(height):
#     for w in range(width-1):
#         print(secondGrid[h][w], end=' ')
#     print(secondGrid[h][width-1])


useless, pics = input().split()
number = input().split('1')
number = number.sorted()
counter = 0
for i in range(int(pics)):
    counter += len(number[i])

print(counter)