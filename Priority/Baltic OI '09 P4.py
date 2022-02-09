from itertools import combinations
from math import sqrt

coords = []

for x in range(int(input())):
    coords.append([int(x) for x in input().split()])

maxArea = 0

for a, b, c, d in combinations(coords, 4):
    center = (a[0]+b[0]+c[0]+d[0])/4, (a[1]+b[1]+c[1]+d[1])/4
    print(a)
    aDist = sqrt((max(a[0], center[0])-min(center[0], a[0]))**2+(max(a[1], center[1]-min(a[1], center[1])))**2)
    print(center)   
    print('distance:', aDist)
    if aDist == sqrt((max(b[0], center[0])-min(center[0], b[0]))**2+(max(b[1], center[1])-min(b[1], center[1]))**2) and aDist == sqrt((max(c[0], center[0])-min(center[0], c[0]))**2+(max(c[1], center[1])-min(c[1], center[1]))**2) and aDist == sqrt((max(d[0], center[0])-min(center[0], d[0]))**2+(max(d[1], center[1])-min(d[1], center[1]))**2):
        maxArea = int(max(maxArea, ((a[0]*b[1]+b[0]*c[1]+c[0]*d[1]+d[0]*a[1])-(a[1]*b[0]+b[1]*c[0]+c[1]*d[0]+d[1]*a[0]))/2))
    print(center[0])

print(maxArea)

    