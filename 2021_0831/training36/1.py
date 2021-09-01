from collections import deque

H,W = map(int,input().split())
A = [list(i for i in input())for _ in range(H)]

d = deque()
for i in range(H):
    for j in range(W):
        if A[i][j]=='#':
            d.append((j,i,0))
dxy = [(1,0),(0,1),(-1,0),(0,-1)]
ans = 0

while d:
    x,y,dist = d.popleft()
    ans = max(ans,dist)
    for dx,dy in dxy:
        if 0<=x+dx<W and 0<=y+dy<H:
            if A[y+dy][x+dx]=='.':
                A[y+dy][x+dx]='#'
                d.append((x+dx,y+dy,dist+1))

print(ans)

