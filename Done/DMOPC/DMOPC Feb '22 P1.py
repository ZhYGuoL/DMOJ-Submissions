length = int(input())
number = input()
for idx in range(length-1):
    if int(number[idx]) < int(number[idx+1]):
        print(number[:idx]+number[idx+1]+number[idx]+number[idx+2:])
        break
    elif idx == length-2:
        print(number)