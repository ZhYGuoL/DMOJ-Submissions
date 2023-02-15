def backwards(string):
    backwards = ""
    for i in range(len(string)):
        backwards += string[-(i + 1)]
    return backwards


def palindromecreator(e):
    palindrome_count = 1
    for i in range(len(e)):
        forwards = e[i:]
        back = forwards[::-1]
        for t in range(len(forwards)):
            if (forwards[t:] in back) or (back[t:] in forwards):
                palindrome_count = max(palindrome_count, len(forwards) - t)
    return palindrome_count


wordgenerator = input().lower()
print(palindromecreator(wordgenerator))