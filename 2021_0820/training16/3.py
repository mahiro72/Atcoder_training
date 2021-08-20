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

N = int(input())
f = list(map(int,input().split()))
uf  = UnionFind(N+1)
mod = 998244353

for i in range(N):
    uf.union(i+1,f[i])

for i in range(N):
    uf.find(i+1)

s = set()
for i,el in enumerate(uf.parents):
    if i==0:
        continue
    if el not in s:
        s.add(el)

print(pow(2,len(s),mod)-1)

