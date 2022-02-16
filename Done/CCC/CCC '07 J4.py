word1 = input()
word2 = input()

counter1 = {}
counter2 = {}

for char in range(len(word1)):
    if word1[char] in counter1:
        counter1[word1[char]] += 1
    else:
        counter1[word1[char]] = 1
    
for char in range(len(word2)):
    if word2[char] in counter2:
        counter2[word2[char]] += 1
    else:
        counter2[word2[char]] = 1

if ' ' in counter1:
    del counter1[' ']
if ' ' in counter2:
    del counter2[' ']

print(counter1)
print(counter2)

for char in counter2:
    if char in counter1 and counter1[char] >= counter2[char]:
        doable = True
    else:
        doable = False
        break

if doable:
    print('Is an anagram.')
else:
    print('Is not an anagram.')