batches = int(input())
even = 0
odd = 0


for cookies in input().split():
    if int(cookies) % 2 == 0:
        even += 1
    else:
        odd += 1

print(odd//2+even//2)