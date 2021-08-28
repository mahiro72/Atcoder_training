class UnionFind:
    def __init__(self,n):
        self.n = n
        self.parents = [-1]*n

    def find(self,x):
        if self.parents[x]<0:
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
        self.parents[x] += self.parents[y]
        self.parents[y] = x

N,M = map(int,input().split())
uf = UnionFind(N+1)
for _ in range(M):
    A,B = map(int,input().split())
    uf.union(A,B)

ans = 0
for i in uf.parents[1:]:
    if i<0:
        ans+=1
        
print(max(ans-1,0))
