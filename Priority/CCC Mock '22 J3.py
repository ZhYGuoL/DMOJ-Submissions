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

print(chars.values())
for char in chars:
    num1, num2 = chars[char]
    # print(num1, num2)
    maxNum = max(maxNum, num1*(num2+1))
    if not num1 and num2 > 0:
        minNum = 0
    elif not num2:
        continue
    else:
        minNum = min(minNum, num1*(num2-1))

crosses = 0
maxFound = False
minFound = False

print(maxNum, minNum)

for num1, num2 in chars.values():
    if num1*(num2+1) == maxNum and not maxFound:
        print(num1, num2)6
        crosses += num1*(num2+1)
    elif num1*(num2-1) == minNum and not minFound:
        crosses += num1*(num2-1)
    else:
        crosses += num1*num2
    

print(crosses)