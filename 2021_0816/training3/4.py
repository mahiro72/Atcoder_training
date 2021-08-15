N,M = map(int,input().split())
S = []
for i in range(M):
    k,*l = map(int,input().split())
    S.append(list(map(lambda x:x-1,l)))
P = list(map(int,input().split()))

ans = 0

for i in range(2**N):
    temp = [0]*N
    for j in range(N):
        if (i>>j)& 1:
            temp[j]=1
    ch = True
    for m in range(M):
        cnt = 0
        for s in S[m]:
            if temp[s]==1:
                cnt+=1
        if cnt%2!=P[m]:
            ch=False
    if ch:
        ans+=1

print(ans)