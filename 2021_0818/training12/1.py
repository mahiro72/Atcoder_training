S = int(input())

def f(x):
    if x%2==0:
        return x//2
    return 3*x+1

m = 1
s = set()
be = S
s.add(be)

while True:
    m += 1
    be = f(be)
    if be in s:
        break
    s.add(be)

print(min(1000000,m))

