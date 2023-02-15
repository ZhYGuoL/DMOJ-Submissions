coins = int(input())
x = int(input())
y = int(input())
z = int(input())
cur = 0
count = 0

while (coins > 0):
    if (cur == 0):
        x = (x + 1) % 35
        cur = (cur + 1) % 3
        if (x == 0):
            coins += 30
    elif (cur == 1):
        y = (y + 1) % 100
        cur = (cur + 1) % 3
        if (y == 0):
            coins += 60
    elif (cur == 2):
        z = (z + 1) % 10
        cur = (cur + 1) % 3
        if (z == 0):
            coins += 9
    coins -= 1
    count += 1
    
print("Martha plays " + str(count) + " times before going broke.")