H,W = map(int,input().split())
cost = [list(map(int,input().split()))for _ in range(10)]
A = [list(map(int,input().split()))for _ in range(H)]

# cost[i][j]: 頂点v_iから頂点v_jへ到達するための辺コスト
for k in range(10):
    for i in range(10):
        for j in range(10):
            cost[i][j] = min(cost[i][j],cost[i][k]+cost[k][j])

ans = 0
for h in range(H):
    for w in range(W):
        if A[h][w]==-1:continue
        ans += cost[A[h][w]][1]

print(ans)





















# import heapq

# H,W = map(int,input().split())
# C = [list(map(int,input().split()))for _ in range(10)]
# A = [list(map(int,input().split()))for _ in range(H)]

# INF = 10**5
# cost = [INF]*10
# cost[1]=0

# def priority(now,goal):
#     magic = INF
#     hq = []
#     heapq.heapify(hq)
#     heapq.heappush(hq,(0,now,0))

#     visited = [[-1]*10 for _ in range(10)]
#     while hq:
#         c,now,m = heapq.heappop(hq)
#         if now==goal:magic = min(m,magic)
#         for nxt in range(10):
#             if visited[now][nxt]<0:
#                 visited[now][nxt] = 1
#                 heapq.heappush(hq,(C[now][nxt],nxt,m+C[now][nxt]))
#     return magic


# for i in range(10):
#     if i==1:continue
#     cost[i] = priority(i,1)

# ans = 0
# for h in range(H):
#     for w in range(W):
#         if A[h][w]==-1:continue
#         ans+=cost[A[h][w]]
# print(ans)
