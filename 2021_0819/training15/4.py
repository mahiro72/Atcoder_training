from math import ceil
from heapq import heappush,heappop

N,M,X,Y = map(int,input().split())
g = [[]for _ in range(N+1)]

for i in range(M):
    A,B,T,K = map(int,input().split())
    g[A].append((B,T,K))
    g[B].append((A,T,K))

def f(start,goal):
    dist = [float("inf")]*(N+1)
    hq = []
    heappush(hq,(0,start))

    while hq:
        d,pos = heappop(hq)
        if dist[pos]<d:
            continue
        dist[pos]=d
        if pos==goal:
            return dist[goal]
        for nxt,t,k in g[pos]:
            if dist[nxt]>ceil(d/k)*k+t:
                heappush(hq,(ceil(d/k)*k+t,nxt))
    return -1

print(f(X,Y))

