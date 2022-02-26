import sys

numItems, limit = [int(x) for x in sys.stdin.readline().strip('\n').split()]
items = []

for _ in range(numItems):
    items.append(input().split())

sorted(items, lambda x: x[1]/x[0])

curCap = 0
curPoints = 0

for _ in range(len(items)):
    if items[0] + counter <= limit:



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