n, k = list(map(int, input().split(' ')))
points = input().split('1')
points.sort(key = len)
L = 0
if k >= len(points):
    for i in points:
        L += len(i)
else:
    for i in range(k):
        L += len(points[-(1+i)])
print(L)