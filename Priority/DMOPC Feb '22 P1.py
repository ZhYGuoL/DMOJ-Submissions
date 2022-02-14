# useless = int(input())
# number = [int(x) for x in input()]

# for i in range(useless-1):
#     if number[i] >= number[i+1]:
#         continue
#     temp = number[i]
#     number[i] = number[i+1]
#     number[i+1] = temp
#     break
# for char in number:
#     print(char, end='')

length = int(input())
number = input()
for idx in range(length-1):
    if int(number[idx]) < int(number[idx+1]):
        print(number[:idx]+number[idx+1]+number[idx]+number[idx+2:])
        break
    elif idx == length-2:
        print(number)