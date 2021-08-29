N, Q = map(int, input().split())
a = list(map(int, input().split()))

class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)
        self.el = [0] * (n + 1)

    def sum(self, i):
        s = 0
        while i > 0:
            s ^= self.data[i]
            i -= i & -i
        return s

    def add(self, i, x):
        self.el[i] ^= x
        while i <= self.n:
            self.data[i] ^= x
            i += i & -i
            
    def get(self, i, j = None):
        if j is None:
            return self.el[i]
        return self.sum(j) ^ self.sum(i)


fwk = BIT(N)

for i in range(N):
    fwk.add(i + 1, a[i])


for _ in range(Q):
    t, x, y = map(int, input().split())
    if t == 1:
        fwk.add(x, y)
    else:
        print(fwk.get(x - 1, y))