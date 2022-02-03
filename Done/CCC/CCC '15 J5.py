def pi(n,k,min):
    if checked [n][k][min] == 0:       
        if n == k:
            checked[n][k][min] = 1
        elif k == 1:
            checked[n][k][min] = 1
        else:
            t = 0
            for i in range (min, int((n / k)+1)):
                t = t + pi(n-i, k-1, i)
            checked[n][k][min] = t
    return checked[n][k][min]



n = int(input())
k = int(input())



checked = [[[0 for _ in range(n+1)]for _ in range(k+1)] for _ in range(n+1)]

print (pi(n,k,1))