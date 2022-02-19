pairsYes = {}
pairsNo = {}

for _ in range(int(input())):
    group = input().split()
    pairsYes[group[0]] = group[1]
    pairsYes[group[1]] = group[0]

for _ in range(int(input())):
    group = input().split()
    if group[0] not in pairsNo:
        pairsNo[group[0]] = list(group[1])
    else:
        pairsNo[group[0]].append(group[1])
    
    if group[1] not in pairsNo:
        pairsNo[group[1]] = list(group[0])
    else:
        pairsNo[group[1]].append(group[0])

counter = 0

for _ in range(int(input())):
    group = input().split()

    for char in group:
        print(pairsYes, pairsNo)
        if char in pairsYes:
            if pairsYes[char] not in group:
                counter += 1
            temp = pairsYes[char]
            del pairsYes[char]
            del pairsYes[temp]
        if char in pairsNo:
            for x in pairsNo[char]:
                if x in group:
                    pairsNo[char].remove(x)
                    counter += 1
        print(pairsYes, pairsNo)
print(int(counter))        

# pairsYes1 = {}
# pairsYes2 = {}
# pairsNo = {}

# for _ in range(int(input())):
#     group = input().split()
#     pairsYes1[group[0]] = group[1]
#     pairsYes2[group[1]] = group[0]
    
# for _ in range(int(input())):
#     group = input().split()
#     pairsNo[group[0]] = group[1]
#     pairsNo[group[1]] = group[0]

# groups = []

# for _ in range(int(input())):
#     group = input().split()

#     for char in group:
#         if char in pairsYes1 or char in pairsYes2 and pairsYes1[char] not in group or pairsYes2[char] not in group:
#             counter += 1
#             del pairsYes[char]
#             del pairsYes[temp]
#         if char in pairsNo and pairsNo[char] in group:
#             counter += 1
#             temp = pairsNo[char]
#             del pairsNo[char]
#             del pairsNo[temp]