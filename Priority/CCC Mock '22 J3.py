chars = {}

useless = input()
for wordNum in range(2):
    for char in input():
        if char in chars:
            chars[char][wordNum] = chars[char][wordNum] + 1
        else:
            if wordNum:
                chars[char] = [0, 1]
            else:
                chars[char] = [1, 0]
  
maxNum = 0
minNum = 6969696969

total = 0

for char in chars:
    num1, num2 = chars[char]
    if num1 > maxNum:
        maxNum = num1
    if num1 < minNum and num2 >= 0:
        minNum = num1
    total += num1*num2


print(total+maxNum-minNum)


# crosses = 0
# maxFound = False
# minFound = False

# print(maxNum, minNum)

# for num1, num2 in chars.values():
#     if num1*(num2+1) == maxNum and not maxFound:
#         print(num1, num2)
#         maxFound = 1
#         crosses += num1*(num2+1)
#     elif num1*(num2-1) == minNum and not minFound:
#         minFound = 1
#         crosses += num1*(num2-1)
#     else: #         crosses += num1*num2
# print(crosses)