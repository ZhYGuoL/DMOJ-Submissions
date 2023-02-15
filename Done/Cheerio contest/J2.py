numPeople, goalLoc = [int(x) for x in input().split()]
goalLoc = int(goalLoc)

closest = ""
minDis = 1000000000

for _ in range(numPeople):
    person, perLoc = input().split()
    perLoc = int(perLoc)
    if (abs(perLoc - goalLoc) < minDis):
        minDis = abs(perLoc - goalLoc)
        closest = person

print(closest)
