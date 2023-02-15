# python program to check if x is a perfect square
import math

# A utility function that returns true if x is perfect square


def isPerfectSquare(x):
	s = int(math.sqrt(x))
	return s*s == x

# Returns true if n is a Fibonacci Number, else false


def isFibonacci(n):

	# n is Fibonacci if one of 5*n*n + 4 or 5*n*n - 4 or both
	# is a perfect square
	return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

for _ in range(int(input())):
	num = int(input())
	flag = False

	if (isFibonacci(num) == True):
		if num <= 4:
			print("NO")
		elif num > 1:
			for i in range(2, num):
				if (num % i) == 0:
					flag = True
					print("YES")
					break
			if flag == False:
				print("NO")
	else:
		print("NO")
