pos = ['1', '2', '3', '4']

for i in input():
    if i == 'V':
        temp = pos[0]
        pos[0] = pos[1]
        pos[1] = temp
        temp = pos[2]
        pos[2] = pos[3]
        pos[3] = temp
    if i == 'H':
        temp = pos[0]
        pos[0] = pos[2]
        pos[2] = temp
        temp = pos[1]
        pos[1] = pos[3]
        pos[3] = temp

print(' '.join(pos[:2]))
print(' '.join(pos[2:]))