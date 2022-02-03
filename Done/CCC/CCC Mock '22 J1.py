k = lambda:int(input())

key = k()
num1 = k()
num2 = k()

if abs(key-num1*num1) < abs(key-num2*num2):
    print(1)
else: print(2)