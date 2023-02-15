# WORKING

while True:
	n = int(raw_input())
	if n == 0:
		break
	coins = list(map(int,raw_input().split()))
	coins = [[x] for x in coins]
	checked = [[] for x in range(n)]
	queue = [[[] for x in range(n)]]
	for i in range(n):
		checked[i] = coins[i]
		queue[0][i] = coins[i]
	ans = 0
	found = False
	print (checked)
	while queue:
		for j in range(len(queue)):
			curr = queue.pop(0)
			if [] not in curr and curr == sorted(curr):
				print (ans)
				found = True
				break
			for i in range(n):
				if len(curr[i])>0:
					if i == 0:
						if curr[i+1] == []:
							temp = [[] for x in range(n)]
							for k in range(n):
								temp[k] = curr[k]
							temp[i+1].append(temp[i].pop())
							if temp not in checked:
								queue.append(temp)
								checked.append(temp)
						elif curr[i][-1] < curr[i+1][-1]:
							temp = [[] for x in range(n)]
							for k in range(n):
								temp[k] = curr[k]
							temp[i+1].append(temp[i].pop())
							if temp not in checked:
								queue.append(temp)
								checked.append(temp)
					elif i == n-1:
						if curr[i-1] == []:
							temp = [[] for x in range(n)]
							for k in range(n):
								temp[k] = curr[k]
							temp[-2].append(temp[i].pop())
							if temp not in checked:
								queue.append([x for x in temp])
								checked.append([x for x in temp])
						elif curr[i][-1] < curr[i-1][-1]:
							temp = [[] for x in range(n)]
							for k in range(n):
								temp[k] = curr[k]
							temp[-2].append(temp[i].pop())
							if temp not in checked:
								queue.append([x for x in temp])
								checked.append([x for x in temp])
					else:
						if curr[i-1] == []:
							temp = [[] for x in range(n)]
							for k in range(n):
								temp[k] = curr[k]
							temp[-2].append(temp[i].pop())
							if temp not in checked:
								queue.append(temp)
								checked.append(temp)
						elif curr[i][-1] < curr[i-1][-1]:
							temp = [[] for x in range(n)]
							for k in range(n):
								temp[k] = curr[k]
							temp[-2].append(temp[i].pop())
							if temp not in checked:
								queue.append(temp)
								checked.append(temp)
						if curr[i+1] == []:
							temp = [[] for x in range(n)]
							for k in range(n):
								temp[k] = curr[k]
							temp[1].append(temp[i].pop())
							if temp not in checked:
								queue.append(temp)
								checked.append(temp)
						elif curr[i][-1] < curr[i+1][-1]:
							temp = [[] for x in range(n)]
							for k in range(n):
								temp[k] = curr[k]
							temp[1].append(temp[i].pop())
							if temp not in checked:
								queue.append(temp)
								checked.append(temp)
		if found:
			break
		ans += 1
	if not found:
		print (checked)
		print ("IMPOSSIBLE")