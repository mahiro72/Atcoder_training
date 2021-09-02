class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s ^= self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] ^= x
            i += i & -i


N,Q = map(int,input().split())
A = list(map(int,input().split()))
bit = Bit(N+1)

for i, a_i in enumerate(A): 
    bit.add(i+1, a_i)

for i in range(Q):
    t,x,y = map(int,input().split())
    if t==1:
        bit.add(x,y)
    else:
        print(bit.sum(y)^bit.sum(x-1))
