# height = int(input())
# width = int(input())

# grid = [[False for _ in range(width)] for _ in range(height)]

# for _ in range(int(input())):
#     direction, pos = input().split(' ')
#     pos = int(pos)-1
#     if direction == 'R':
#         for i in range(width):
#             grid[pos][i] = not grid[pos][i]

#     else:
#         for i in range(height):
#             grid[i][pos] = not grid[i][pos]

# counter = 0
# print(grid)

# for i in range(height):

#     for x in range(width):

#         if grid[i][x]:
#             counter += 1

# print(counter)



# ^^^^^^ TLE last batch
#==================================
# The one below also TLE lmao



# row = int(input())
# col = int(input())

# canvas = [False for _ in range(row*col)]

# for i in range(int(input())):
#     paint = str(input()).split(' ')
#     J = ((int(paint[1])-1))
#     if paint[0] == "row":
#         for e in range(col):
            
#             canvas[J*col+e] = not canvas[J*col+e]
    
#     else:
#         for a in range(row):
            
#             canvas[J+col*a] = not canvas[J+col*a]

# count = 0

# for x in range(len(canvas)):
#     count += int(canvas[x])

# print(count)


# ===========================
# Bottom one works like a charm (4 secs)


# k = lambda:int(input())
# height = k()
# width = k()

# Rlines = {}
# Clines = {}

# for i in range(k()):
#     line, pos = input().split(' ')
#     if line == 'R':
#         if pos in Rlines:
#             del Rlines[pos]
#         else:
#             Rlines[pos] = 0

#     else:
#         if pos in Clines:
#             del Clines[pos]
#         else:
#             Clines[pos] = 0

# rows = len(Rlines)
# columns = len(Clines)

# print(rows*width + columns*height - 2*rows*columns)

# ============================
# Code below is fastest

k = lambda:int(input())
height = k()
width = k()

lines = {}

for i in range(k()):
    line = input()
    temp.append(line)
    if line not in lines:
        lines[line] = 0
    else:
        del lines[line]

rows = 0
columns = 0

for item in lines:
    if item[0] == 'R':
        rows += 1
    else:
        columns += 1

print(rows*width + columns*height - 2*rows*columns)