import sys

size = int(sys.stdin.readline())

pizza = [0 for x in range(size)]

ep, ed = [int(x) for x in input().split()]

for _ in range(int(input())):
    start, end = [int(x) for x in input().split()]
    
    if end == size:
        pizza[start] += 1
        
    else:
        pizza[start] += 1
        pizza[end+1] -= 1
        
updated = [pizza[0]]        

for idx in range(1, size):
    updated.append(updated[idx-1]+pizza[idx])

counter = 0
for x in range(ep, ed+1):
    counter += updated[x]
    
print(counter)