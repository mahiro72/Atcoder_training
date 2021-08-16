N = int(input())
F = [list(map(int,input().split()))for _ in range(N)]
P = [list(map(int,input().split()))for _ in range(N)]

ans = -float("inf")
for i in range(2**10):
    bit = [0]*10
    if i==0:
        continue
    for j in range(10):
        if (i>>j)& 1:
            bit[j]=1
    temp = 0
    for x in range(N):
        cnt = 0
        for b in range(10):
            if bit[b]==1 and F[x][b]==1:
                cnt+=1
        temp+=P[x][cnt]
    ans = max(ans,temp)
print(ans)