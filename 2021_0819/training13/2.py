import sys
sys.setrecursionlimit(10**6)

H,W = map(int,input().split())
A = [input()for _ in range(H)]
visited = [[-1]*W for _ in range(H)]
dxy = [(1,0),(0,1)]

def dfs(now,goal,time):
    global visited 
    x,y = now
    visited[y][x] = time
    if x==goal[0] and y==goal[1]:
        return
    for dx,dy in dxy:
        if 0<=x+dx<W and 0<=y+dy<H:
            if A[y+dy][x+dx]=="#" and visited[y+dy][x+dx]==-1:
                dfs((x+dx,y+dy),goal,time+1)


dfs((0,0),(W-1,H-1),0)
time_list = set()
cnt = 0

for h in range(H):
    for w in range(W):
        if A[h][w]=="#":
            cnt+=1
            if visited[h][w]==-1:
                exit(print("Impossible"))
            time_list.add(visited[h][w])

if len(time_list)==cnt:
    print("Possible")
else:
    print("Impossible")
