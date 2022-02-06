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


NumObstacles, aHeight, bHeight = [int(x) for x in input().split()]

aTemp = 0
bTemp = 0

for _ in range(NumObstacles):
    obs1, obs2 = [int(x) for x in input().split()]
    if obs1 < aHeight:
        aTemp += 1
    else:
        aTemp += 2
    if obs2 < bHeight:
        bTemp += 1
    else:
        bTemp += 2

if aTemp > bTemp:
    print('Tommy wins!')
elif aTemp < bTemp:
    print('Andrew wins!')
else:
    print('Tie!')