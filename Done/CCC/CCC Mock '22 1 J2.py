speed = int(input().split(' ')[1])
counter = 0


for char in input():
    if char == 'F':
        if speed == 0:
            counter += 1
    elif char == 'D':
        speed += 1
    else:
        if speed >= 1:
            speed -= 1
        if speed == 0:
            counter += 1

print(counter)