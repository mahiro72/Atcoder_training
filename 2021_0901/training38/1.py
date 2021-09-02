N,M = map(int,input().split())
g = [[]for _ in range(N)]
inv = [0]*N
s = []

for _ in range(M):
    k = int(input())
    a = list(map(lambda x: int(x)-1,input().split()))
    for i in range(k-1):
        g[a[i]].append(a[i+1])
        inv[a[i+1]] +=1


for i in range(N):
    if inv[i]==0:s.append(i)

while s:
    p = s.pop()
    for node in g[p]:
        inv[node]-=1
        if inv[node]==0:s.append(node)

if max(inv)>0:
    print('No')
else:
    print('Yes')
    