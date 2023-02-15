import sys

s = 0
t = 0


for _ in range(int(sys.stdin.readline())):
    sen = sys.stdin.readline().lower()
    s += sen.count('s')
    t += sen.count('t')

if (s >= t):
    print("French")

else:
    print("English")
