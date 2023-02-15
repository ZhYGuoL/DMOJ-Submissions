def maxSquare(M):
	R = len(M) 
	C = len(M[0]) 

	S = []
	for i in range(R):
		temp = []
		for j in range(C):
			if i==0 or j==0:
				temp += M[i][j],
			else:
				temp += 0,
		S += temp,

	for i in range(1, R):
		for j in range(1, C):
			if (M[i][j] == 1):
				S[i][j] = min(S[i][j-1], S[i-1][j], S[i-1][j-1]) + 1
			else:
				S[i][j] = 0
	
	max_of_s = S[0][0]
	max_i = 0
	max_j = 0
	for i in range(R):
		for j in range(C):
			if (max_of_s < S[i][j]):
				max_of_s = S[i][j]
				max_i = i
				max_j = j

	counter = 0

	for i in range(max_i, max_i - max_of_s, -1):
		counter += 1

	print(counter)

size = int(input())

M = [[1 for _ in range(size)] for _ in range(size)]

for _ in range(int(input())):
	y, x = [int(x) for x in input().split()]

	M[y-1][x-1] = 0

maxSquare(M)



# coords = {}

# size = int(input())

# for _ in range(int(input())):
# 	coord = [int(x) for x in input().split()]

# 	if coord[0] in coords:
# 		coords[coord[0]].append(coord[1])
# 	else:
# 		coords[coord[0]] = [coord[1]]

# print(coords)



# def possibilities(key, size):
# 	posSize = 0
# 	a = 1
# 	while key + a <= size:
# 		if range(key+a):


# for key in coords:
# 	print('bruh')