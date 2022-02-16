individual = [0]*2001
pair = [0]*4001

useless = int(input())

for num in input().split():
    num = int(num)
    
    individual[num] += 1

for i in range(len(individual)-1):
    for n in range(i, len(individual)):
        if i == n:
            pair[i + n] += individual[i] / 2
        
        else:
            pair[i + n] += min(individual[i], individual[n])

biggest = 0
size = 0


for height in pair:
    if height > biggest:
        size = 1
        biggest = height
    elif height == biggest:
        size += 1

print(int(biggest), size)