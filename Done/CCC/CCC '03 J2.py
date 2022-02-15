from math import floor

while True:
    number = int(input())
    if number == 0:
        break
    else:
        root = floor(number**(1/2))
        print('Minimum perimeter is ' + str(2*(int((number/root)))+2*(root)) + ' with dimensions ' + str(int(number/root))+ ' x ' +  str(root))