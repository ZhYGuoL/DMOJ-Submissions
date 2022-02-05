time = int(input())

times = []
x = int(input())

for i in range(x):

    times.append(int(input()))

times.sort()
counter = 0
for i in range(x):
    if time - times[i]>=0:
        counter+=1
        time-=times[i]
    else:
        break
print(counter)