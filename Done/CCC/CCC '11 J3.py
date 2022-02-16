num1 = int(input())
num2 = int(input())

counter = 0

while num2 >= num1 - num2:
    counter += 1
    temp = num1
    num1 = num2
    num2 = temp - num2

print(counter + 3)