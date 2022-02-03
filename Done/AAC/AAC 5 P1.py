from math import floor

batches = int(input())
even = 0
odd = 0

for cookiesInBatch in input().split(' '):
    if int(cookiesInBatch) % 2 == 0:
        even += 1
    else:
        odd += 1

print(floor(even/2)+floor(odd/2))