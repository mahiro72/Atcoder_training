H,W,N,M = map(int,input().split())

g = [[0]*W for _ in range(H)]
for i in range(N):
    A,B = map(int,input().split())
    g[A-1][B-1] = 1
for i in range(M):
    C,D = map(int,input().split())
    g[C-1][D-1] = -1

ans=0
for i in range(H):
    for j in range(W):
        if g[i][j]==1:
            now = j
            while now+1<W and g[i][now+1]==0:
                now+=1
                g[i][now]=2
                ans+=1
            now = j
            while 0<=now-1 and g[i][now-1]==0:
                now-=1
                g[i][now]=2
                ans+=1


for i in range(W):
    for j in range(H):
        if g[j][i]==1:
            now = j
            while now+1<H and g[now+1][i]!=-1:
                now+=1
                if g[now][i]!=2:
                    ans+=1
                    g[now][i]=2
                
            now = j
            while 0<=now-1 and g[now-1][i]!=-1:
                now-=1
                if g[now][i]!=2:
                    ans+=1
                    g[now][i]=2

print(ans+N)
