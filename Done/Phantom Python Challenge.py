l = input()
for i in sorted(set(range(2,l)).difference(a for i in range(2,l) for a in range(2,l) if a!=i and a%i == 0)): print (i)

for i in lambda n: set(range(2,n)) - set([i for q in range(2,int(n**0.5)) for i in range(q*2,n,q)])(10): print (i)