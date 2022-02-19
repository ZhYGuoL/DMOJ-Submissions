from math import atan, degrees

def angle(coord1, coord2):
    angle = degrees(atan2(abs(coord1[0]-coord2[0]), abs(coord1[1]-coord2[1])))
    
    if angle < 0:
        return True
    elif angle > 0:
        return False
    else:
        return True

numCoords, radius = [int(x) for x in input().split()]

coords = []

for _ in range(numCoords):
    coords.append([int(x) for x in input().split()])

sorted(coords, key = lambda x: x[0])

print(coords)

top = [coords[0], coords[1]]
bottom = []

for coord in coords:
    while angle(coords[-1], coords[-2])
