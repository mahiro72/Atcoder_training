class UnionFind:
    def __init__(self,n):
        self.n = n
        self.parents = list(range(self.n))
    
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
A = list(map(int,input().split()))
B = list(map(int,input().split()))

uf = UnionFind(N+1)

for i in range(M):
    c,d = map(int,input().split())
    uf.union(c,d)

for i in range(1,N+1):
    uf.find(i)

dic1 = {x:0 for x in range(N+1)}
dic2 = {x:0 for x in range(N+1)}

for i,par in enumerate(uf.parents):
    if i==0:
        continue
    dic1[par] += A[i-1]
    dic2[par] += B[i-1]

if dic1==dic2:
    print("Yes")
else:
    print("No")