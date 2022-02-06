numObstacles, a, b = [int(x) for x in input().split()]

aTime = 0
bTime = 0

for _ in range(numObstacles):
    aObs, bObs = [int(x) for x in input().split()]
    if aObs < a:
        aTime += 1
    else:
        aTime += 2
    if bObs < b:
        bTime += 1
    else:
        bTime += 2

if aTime > bTime:
    print('Tommy wins!')
elif aTime < bTime:
    print('Andrew wins!')
else:
    print('Tie!')