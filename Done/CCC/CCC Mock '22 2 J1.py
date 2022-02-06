prices = input().split()
people = input().split()

totalPeople = 0
totalPrice = 0
for i in range(3):
    totalPeople += int(people[i])
    totalPrice += int(people[i])*int(prices[i])

print(totalPeople, totalPrice)