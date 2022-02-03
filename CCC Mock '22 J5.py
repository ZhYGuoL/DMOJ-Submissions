lines = int(input().split()[1])

print(lines)

resolutions = {}

for _ in range(lines):
    for num in input().split(' '):
        if num in resolutions:
            resolutions[num] += 1
        else:
            resolutions[num] = 1

print(int(max(resolutions, key=resolutions.get)))
print(resolutions)




lines = int(input().split(' '))

usedResolutions = {}
invalidDoableResolutions = {}


for _ in range(lines):
    stillDoable = 1
    for num in input().split(' '):
        if num in usedResolutions:
            if stillDoable == 1:
                stillDoable = 0

            else:
                break

    
            