import sys

n, k = [int(x) for x in sys.stdin.readline().split()]

answers = {}

for _ in range(n):
    for idx, char in enumerate(sys.stdin.readline().strip('\n')):
        if idx not in answers:
            answers[idx] = [char == 'T']
        elif (char == 'T') in answers[idx]:
            continue
        elif (char != 'F') in answers[idx]:
            continue
        else:
            answers[idx].append(char == 'T')

counter = 0

for key in range(k):
    if len(answers[key]) == 1:
        counter += 1

print(counter)