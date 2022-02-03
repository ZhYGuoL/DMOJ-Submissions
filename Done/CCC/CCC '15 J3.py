newWord = ''
vowels = {'a', 'e', 'i', 'o', 'u'}
word = input()
for char in word:

    if char in vowels:
        newWord += char
        continue

    newWord += char
    unicode = ord(char)

    closestVowel = min(abs(97-unicode), abs(101-unicode), abs(105-unicode), abs(111-unicode), abs(117-unicode))

    if chr(unicode-closestVowel) in vowels:
        newWord += chr(unicode-closestVowel)

    else:
        newWord += chr(unicode+closestVowel)

    if char == 'z':
        newWord += 'z'
    elif chr(unicode+1) in vowels:
        newWord += chr(unicode+2)
    else:
        newWord += chr(unicode+1)


print(newWord)




newWord = ''
for char in input():
    if char == 'a':
        newWord+='a'
        continue
    if char == 'b':
        newWord+='bac'
        continue
    if char == 'c':
        newWord+='cad'
        continue
    if char == 'd':
        newWord+='def'
        continue
    if char == 'e':
        newWord+='e'
        continue
    if char == 'f':
        newWord+='feg'
        continue
    if char == 'g':
        newWord+='geh'
        continue
    if char == 'h':
        newWord+='hij'
        continue
    if char == 'i':
        newWord+='i'
        continue
    if char == 'j':
        newWord+='jik'
        continue
    if char == 'k':
        newWord+='kil'
        continue
    if char == 'l':
        newWord+='lim'
        continue
    if char == 'm':
        newWord+='mon'
        continue
    if char == 'n':
        newWord+='nop'
        continue
    if char == 'o':
        newWord+='o'
        continue
    if char == 'p':
        newWord+='poq'
        continue
    if char == 'q':
        newWord+='qor'
        continue
    if char == 'r':
        newWord+='ros'
        continue
    if char == 's':
        newWord+='sut'
        continue
    if char == 't':
        newWord+='tuv'
        continue
    if char == 'u':
        newWord+='u'
        continue
    if char == 'v':
        newWord+='vuw'
        continue
    if char == 'w':
        newWord+='wux'
        continue
    if char == 'x':
        newWord+='xuy'
        continue
    if char == 'y':
        newWord+='yuz'
        continue
    if char == 'z':
        newWord+='zuz'
        continue

print(newWord)