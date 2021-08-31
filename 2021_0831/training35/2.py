N,M = map(int,input().split())

xy = [list(map(lambda x:int(x)-1,input().split()))for _ in range(M)]
flag = [0]*N
flag[0]=1
cnt = [1]*N

for x,y in xy:
    cnt[x]-=1
    cnt[y]+=1
    if flag[x]==1:flag[y]=1
    if cnt[x]==0:flag[x]=0
    
print(sum(flag))