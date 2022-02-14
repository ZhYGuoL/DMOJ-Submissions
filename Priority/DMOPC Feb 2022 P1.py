useless = int(input())
number = [int(x) for x in input()]

for i in range(useless-1):
    if number[i] >= number[i+1]:
        continue
    temp = number[i]
    number[i] = number[i+1]
    number[i+1] = temp
    break
for char in number:
    print(char, end='')