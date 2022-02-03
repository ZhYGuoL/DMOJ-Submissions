num = int(input())
x = int(input())

mod = num % x

if not mod:
    print(0)
if (num / x < 2):
    print(x - mod)
else: print(min(x - mod, mod))

# vvvvv Better code

n = int(input())
k = int(input())

if (n > k):
    print(min(n % k, k - n % k))
else:
    print(min(k, k - n))