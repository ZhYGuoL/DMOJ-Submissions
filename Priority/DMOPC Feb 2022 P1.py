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

length = int(input())
num = map(int, input())

for idx in range(length):
    if idx == 0:
        continue
    if number[idx] >= number[idx+1]:
        print(str(number[:idx-1])+str(number[idx+1])+str(number[idx])+str(number[idx+2:]))