import sys

size, flips = [int(x) for x in sys.stdin.readline().strip('\n').split()]

board = [[[0]*size]*size]

for _ in flips