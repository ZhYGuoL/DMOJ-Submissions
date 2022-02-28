import sys

n, k = [int(x) for x in sys.stdin.readline().split()]


men = [int(x) for x in sys.stdin.readline().split()] 
men = sorted(men, reverse=True)

women = [int(x) for x in sys.stdin.readline().split()] 
women = sorted(women, reverse=True)

counter = 0

for idx in range(1, n):
    counter = (counter+men[idx]*women[idx]) % 1000000007


if abs(men[0]-women[0]) > k:
    counter = (counter+(min(men[0], women[0])+k)*max(men[0], women[0]))  % 1000000007
else:
    if men[0] < women[0]:
        k -= abs(men[0]-women[0])
        men[0] = women[0]

    else:
        k -= abs(men[0]-women[0])
        women[0] = men[0]

    if k % 2 == 0:
        counter = (counter+(int(men[0]+(k/2))*int(women[0]+(k/2))))  % 1000000007

    else:
        counter = (counter+((men[0]+int(k/2+0.5))*(women[0]+int(k/2-0.5)))) % 1000000007
    


print(counter)