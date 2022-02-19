square, circle = [int(x) for x in input().split()]

if square**2 > (circle**2)*3.14159265359:
    print('SQUARE')
else:
    print('CIRCLE')