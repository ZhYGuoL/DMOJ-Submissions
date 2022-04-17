word = input().lower()
biggest = 0
for i in range(len(word) + 1):
    for n in range(len(word) + 1):
        curWord = word[i:n]
        if curWord[::-1] == curWord:
            biggest = max(len(curWord), biggest)

print(int(biggest))