from collections import deque
N, M = map(int, input().split())
arrA = list(map(int, input().split()))
arrXY = [list(map(int, input().split())) for i in range(M)]

path = [[] for _ in range(N)]
for x, y in arrXY:
	path[x - 1].append(y - 1)

result = -float("inf")
seen = [-1] * N
que = deque([])

for i, val in sorted(enumerate(arrA), key=lambda x: x[1]):
	if seen[i] != -1:
		continue

	que.append(i)
	while len(que) > 0:
		v = que.popleft()

		for next_v in path[v]:
			if seen[next_v] != -1:
				continue
			
			seen[next_v] = 0
			result = max(result, arrA[next_v] - arrA[i])
			que.append(next_v)

print(result)