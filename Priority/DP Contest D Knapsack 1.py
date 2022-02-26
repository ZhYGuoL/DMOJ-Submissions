import sys

numItems, limit = [int(x) for x in sys.stdin.readline().strip('\n').split()]
items = []

for _ in range(numItems):
    items.append([int(x) for x in sys.stdin.readline().strip('\n').split()])
    
# print(items)

items = sorted(items, key=lambda x: x[1]/x[0], reverse=True)

curCap = 0
curPoints = 0

print(items)

for idx in range(len(items)):
    items[idx]
    if items[idx][0] + curCap <= limit:
        curCap += items[idx][0]
        curPoints += items[idx][1]
        if curCap == limit:
            break
        

print(curPoints)        



# 3 8
# 3 30
# 4 50
# 5 60

# 90



# 5 5
# 1 1000000000
# 1 1000000000
# 1 1000000000
# 1 1000000000
# 1 1000000000

# 5000000000



# 6 15
# 6 5
# 5 6
# 6 4
# 6 6
# 3 5
# 7 2

# 17