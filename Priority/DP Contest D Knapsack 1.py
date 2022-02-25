import sys

numItems, limit = [int(x) for x in sys.stdin.readline().strip('\n').split()]
items = []

for _ in range(numItems):
    items.append(input().split())

sorted(items, lambda x: x[1]/x[0])