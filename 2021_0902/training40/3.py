N = int(input())
def idx(s):
    return ord(s)-97

class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)

    def sum(self, i):
        s = 0
        i += 1
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

d = {}
for i in range(26):
    d[i] = BIT(N)

S = input()
for i in range(N):
    d[idx(S[i])].add(i,1)
S = list(S)

Q = int(input())
for _ in range(Q):
    q = input().split()
    if q[0]=='1':
        i = int(q[1])-1
        s = S[i]
        d[idx(s)].add(i,-1)
        S[i] = q[2]
        d[idx(q[2])].add(i,1)
    else:
        l,r = int(q[1])-1,int(q[2])-1
        res = 0
        for i in range(26):
            c = d[i].sum(r)
            if l!=0:
                c -= d[i].sum(l-1)
            c = min(1,c)
            res += c
        print(res)