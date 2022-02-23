import sys

a, b, c, d, e = [int(x) for x in sys.stdin.readline().strip('\n').split()]
print(a*5 + b*10 + c*25 + d*100 + e*200)