from math import sqrt

allNumbersCombined = 0

N = int(input())

print('? 1 2')

zeroxOne = int(input())

print('? 1 3')

zeroxTwo = int(input())

print('? 2 3')

onexTwo = int(input())

num1 = int(sqrt(zeroxOne*zeroxTwo/onexTwo))
num2 = int(zeroxOne/num1)
num3 = int(onexTwo/(zeroxOne/num1))
allNumbersCombined += num1 + num2 + num3
prevNum = num3
numbersArranged = str(num1) + ' ' + str(num2) + ' ' + str(num3) + ' '


for curNum in range(4, N):
    print('? ' + str(curNum-1) + ' ' + str(curNum))

    prevNum = int(int(input())/prevNum)

    numbersArranged += str(prevNum) + ' '

    allNumbersCombined += prevNum

a = 0
for i in range(N+1):
    a += i

print('! '+ numbersArranged + str(int(a-allNumbersCombined)))