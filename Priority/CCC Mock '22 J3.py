chars = {}

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

print(chars)
for char in chars:
    if chars[char][0] >= maxNum:
        maxNum = chars[char][0]
    elif chars[char][0] <= minNum and chars[char][1] >= 0:
        minNum = chars[char][0]
    total += chars[char][0]*chars[char][1]

print(pair1, pair2)

# print(total+(pair1[0]*(pair1[1]+1)-pair1[0]*pair[1]))
print(total+pair1[0]-pair2[0])


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