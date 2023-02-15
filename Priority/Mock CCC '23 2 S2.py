import sys

t1 = []
t2 = []

minNum = 69696969696969
biggestNums = []

for _ in range(int(sys.stdin.readline())):
    cur = int(sys.stdin.readline())
    if len(biggestNums) < 12:
        biggestNums.append(cur)
        minNum = min(cur, minNum)
    elif cur >= minNum:
        biggestNums.append(cur)
        biggestNums.remove(minNum)
        minNum = min(biggestNums)
    print(biggestNums)
biggestNums.sort()

print(biggestNums)
print(minNum)

# testcases = int(sys.stdin.readline())

# for _ in range(6):
#     cur = int(sys.stdin.readline())
#     if len(biggestNums) < 6:
#         biggestNums.append(cur)
# biggestNums.sort()

# t1, t2 = biggestNums[:3], biggestNums[3:]

# print(t2)