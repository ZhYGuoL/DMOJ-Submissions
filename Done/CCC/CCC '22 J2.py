counter = 0

players = int(input())

for _ in range(players):
    score = 0
    score += int(input())*5
    score -= int(input())*3

    if score > 40:
        counter += 1

if counter == players:
    print(str(counter) + '+')
else:
    print(counter)


