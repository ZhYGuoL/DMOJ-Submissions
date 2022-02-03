# https://dmoj.ca/problem/ccc21s1

testcases = int(input())

heights = [int(x) for x in input().split(' ')]
widths = [int(x) for x in input().split(' ')]

area = 0

for idx, width in enumerate(widths):
    area += (min(heights[idx], heights[idx+1]) * width) + (abs(heights[idx]-heights[idx+1]) * width /2)

print(area)