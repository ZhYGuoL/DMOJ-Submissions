n = int(input())
pts = set()
best = 0

for _ in range(n):
  
    pts.add(tuple(map(int, input().split(' '))))


for i in pts:
    x1, y1 = i
    for j in pts:
        x2, y2 = j


        if (x1, y2) in pts and (x2, y1) in pts:
            best = max(best, abs(x2 - x1) * abs(y2 - y1))

print(best)