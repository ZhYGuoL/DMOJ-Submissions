coord1 = [int(x) for x in input().split()]
coord2 = [int(x) for x in input().split()]
charge = int(input())
dist = abs(coord1[0]-coord2[0]) + abs(coord1[1]-coord2[1])
if charge >= dist and (charge - dist) % 2 == 0:
    print('Y')
else:
    print('N')