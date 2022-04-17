b, c, d, e = [int(x) for x in input().split()]
a = 0


print(0, a+b, a+b+c, a+b+c+d, a+b+c+d+e)
print(b, 0, c, c+d, c+d+e)
print(c+b, c, 0, d, d+e)
print(d+c+b, d+c, d, 0, e)
print(e+d+c+b, c+e+d, d+e, e, 0)

# different solution vvv

numbers = [int(x) for x in input("enter space-separated numbers").split()]

firstRow = [0]
for i in range(len(numbers)):
    firstRow.append(firstRow[i] + numbers[i])

for i in range(len(numbers) + 1):
    currentRow = []
    for j in range(len(numbers) + 1):
        distance = firstRow[j] - firstRow[i]
        currentRow.append(abs(distance))
    print(*currentRow)