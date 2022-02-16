temp = {}
friends = {}

for _ in range(int(input())):
    msgType, friend = input().split()

    if msgType == 'W':
        for x in temp:
            temp[x] += int(friend)-1
    elif msgType == 'R':
        if friend in temp:
            friends[friend] = -1
        else:
            temp[friend] = 0
            if friend not in friends:
                friends[friend] = 0
        for x in temp:
            temp[x] += 1
    else:
        if friend not in temp:
            friends[friend] = -1
        else:
            if friends[friend] != -1:
                friends[friend] += temp[friend]
        temp.pop(friend)
        for x in temp:
            temp[x] += 1

for x in temp:
    friends[x] = -1

for x in sorted(friends.keys()):
    print(x, friends[x])