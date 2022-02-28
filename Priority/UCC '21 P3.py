import sys

pizzaSize = int(sys.stdin.readline())

area = [int(x) for x in sys.stdin.readline().split()]

for _ in range(int(sys.stdin.readline())):
    op, ed = [int(x) for x in sys.stdin.readline().split()]

    if range(area[0], area[1])