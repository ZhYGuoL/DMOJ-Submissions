maxGroup = int(input())

people = {}
print(people)

for i in range(int(input())):
    person = input()
    people[person] = int(input())

# sort people by value
people = (dict(sorted(people.items(), key=lambda x: x[1])))
names = list(people.keys())

time = 0
print(people)
print(names)
groups = []

for i in range(0, len(people), maxGroup):
    time += people[names[0]]
    names = names[maxGroup:]
    
print('Total Time: ' + str(time))

print(groups)

# split names into groups of maxGroup 

# groups.append(names[len(names) - maxGroup:])
# for i in range(len(names) - maxGroup):

if len(names) <= maxGroup:
    print(' '.join(names))
else:
    for i in range(0, len(names)-(len(names)%maxGroup), maxGroup):
        groups.append(names[i:i+maxGroup])
    groups.append(names[len(names)-len(names)%maxGroup:])
    print(groups)