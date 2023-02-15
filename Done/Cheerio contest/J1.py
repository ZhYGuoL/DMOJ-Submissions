vowels = ['a', 'e', 'i', 'o', 'u']

word = input()
prevVowel = None
done = False

for char in word:
    if ((char in vowels) != prevVowel):
        prevVowel = (char in vowels)
    else:
        done = True
        break
if done == False:
    print('YES')
else:
    print('NO')