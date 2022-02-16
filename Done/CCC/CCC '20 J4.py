largeString = input()
key = input()

shift = 0

for _ in range(len(key)):
    if key in largeString:
        shift = 1
        break
    key = key[-1]+key[:-1]
    print(key)

if shift:
    print('yes')
else:
    print('no')