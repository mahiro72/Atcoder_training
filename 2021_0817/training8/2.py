class UnionFind:
    def __init__(self,n):
        self.n = n
        self.parents = list(range(n))
    
    def find(self,x):
        if self.parents[x]==x:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self,x,y):
        x = self.find(x)
        y = self.find(y)
        if x==y:
            return
        if self.parents[x]>self.parents[y]:
            x,y = y,x
        self.parents[y] = x
        

N,M = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
uf = UnionFind(N+1)

for i in range(M):
    c,d = map(int,input().split())
    uf.union(c,d)

for i in range(1, N+ 1):
    uf.find(i)

dic1 = {x:0 for x in range(1,N+1)}
dic2 = {x:0 for x in range(1,N+1)}

for i,par in enumerate(uf.parents):
    if i==0:
        continue
    dic1[par]+=a[i-1]
    dic2[par]+=b[i-1]

if dic1==dic2:
    print("Yes")
else:
    print("No")





























# from collections import deque

# N,M = map(int,input().split())
# A = [0]+list(map(int,input().split()))
# B = [0]+list(map(int,input().split()))
# dif = [0]
# for i in range(N):
#     dif.append(B[i]-A[i])

# g = [[]for _ in range(N+1)]

# for _ in range(M):
#     c,d = map(int,input().split())
#     g[c].append(d)
#     g[d].append(c)

# def bfs(start):
#     d = deque()
#     d.append(start)
#     visited = [False]*(N+1)
#     while d:
#         pos = d.popleft()
#         visited[pos] = True
#         s = set()
#         for nxt in g[pos]:
#             if visited[nxt]==False:
#                 s.add(dif[nxt])
#         print(s)
#         if len(s)<=1:
#             for nxt in g[pos]:
#                 if visited[nxt]==False:
#                     d.append(nxt)
#         else:
#             print("##",s)
#             exit(print("No"))

# bfs(1)
# print("Yes")
