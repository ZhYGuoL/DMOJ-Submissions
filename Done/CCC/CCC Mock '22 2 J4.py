# numTeams, groupSize = [int(x) for x in input().split()]
# groups = [[] for x in range(int(numTeams/groupSize))]

# # [
# #     {},
# #     {},
# #     {}
# # ]

# # def findWinner():







# for i in range(int(numTeams/groupSize)):
#     groups = [[] for x in range(int(numTeams/groupSize))]
#     for x in input().split():
#         a = {x: [0, '']}
#         groups[i].append(a.copy())

#     for o in range(sum([p for p in range(1, groupSize)])):
#         a, b, result = input().split()

# # for i in rang(int(numTeams/groupSize)):


# print(groups)



from math import factorial

numTeams, groupSize = [int(x) for x in input().split()]

teams = {}
a = input().split()
for x in a:
    teams[int(x)] = 0

# def permutation(groupSize):
#     a = 0
#     for x in range(1, groupSize):
#         a += x
    
#     return a


for o in range(factorial(groupSize)):
    a, b, result = input().split()
    a = int(a)
    b = int(b)

    if result == 'W':
        teams[a] = teams[a] + 3
    elif result == 'L':
        teams[b] = teams[b] + 3
    else:
        teams[a] = teams[a] + 1
        teams[b] = teams[b] + 1

sortedRankings = list({k: v for k, v in sorted(teams.items(), key=lambda item: item[1])}.keys())[-1*int(input())]
print(sortedRankings)