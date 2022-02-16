points = [100, 100]

for _ in range(int(input())):
    roll1, roll2 = [int(x) for x in input().split()]

    if roll1 > roll2:
        points[1] -= roll1
    elif roll1 < roll2:
        points[0] -= roll2

print(points[0])
print(points[1])