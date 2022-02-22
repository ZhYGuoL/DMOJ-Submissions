import sys

mass = [int(sys.stdin.readline()) for x in range(int(sys.stdin.readline()))]

updated = [mass[0]]

for idx in range(1, len(mass)):
    updated.append(updated[-1]+mass[idx])

for _ in range(int(sys.stdin.readline())):
    op, ed = [int(x) for x in sys.stdin.readline().split()]
    if op == 0:
        print(updated[ed])
    else:
        print(updated[ed]-updated[op-1])