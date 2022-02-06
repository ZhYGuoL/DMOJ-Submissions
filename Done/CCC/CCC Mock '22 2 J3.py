N = int(input())

scores = [int(x) for x in input().split()]

half = sum(scores)/2

left, right = 0, 0
idx = 0
counterLeft, counterRight = 0, 0

for i in range(N):
    
    if left+scores[i] <= half:

        counterLeft += 1
        idx += 1
        left+=scores[i]
        if right+scores[-1*(i+1)] <= half:
            counterRight += 1
            right+=scores[-1*(i+1)]
    else:
        if right+scores[-1*(i+1)] <= half:

            counterRight += 1
            right+=scores[-1*(i+1)]
        else:
            if left == right and (counterLeft+counterRight)/2 == N/2:
                print(idx)
                break
            else:
                print('Andrew is sad.')
                break