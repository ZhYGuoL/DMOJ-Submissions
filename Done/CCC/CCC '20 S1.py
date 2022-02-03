# https://dmoj.ca/problem/ccc20s1

values = {}

for _ in range(int(input())):
    testcase = input().split(' ')
    values[int(testcase[0])] = int(testcase[1])

minSpeed = 0

sortedValues = dict(sorted(values.items()))
prev = None

for x in sortedValues:
    if prev == None:
        prev = x
        continue
    minSpeed = max(minSpeed, (abs(values[prev]-values[x]))/(abs(prev-x)))
    prev = x
print(round(minSpeed, 1))