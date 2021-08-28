N,M,X = map(int,input().split())

l = []
ans = float('inf')

for _ in range(N):
    c,*a = map(int,input().split())
    l.append((c,list(a)))

for i in range(2**N):
    bit = [0]*N
    for j in range(N):
        if (i>>j)&1:
            bit[j]=1
    
    ch = [0]*M
    cost = 0
    for k in range(N):
        if bit[k]==1:
            c,a = l[k]
            cost += c
            for m in range(M):
                ch[m]+=a[m]
    flag = True
    for c in ch:
        if c<X:
            flag = False
            break
    if flag:
        ans = min(ans,cost)

if ans!=float('inf'):
    print(ans)
else:
    print(-1)