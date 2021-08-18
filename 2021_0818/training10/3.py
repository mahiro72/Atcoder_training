A,B = map(int,input().split())

def f(x):
    s = set()
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            s.add(x//i)
            s.add(i)
    return s

def is_prime(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return 0
    return 1

l = list(f(A)&f(B))
if len(l)==1:
    exit(print(1))

ans = []
for i in l:
    if is_prime(i):
        ans.append(i)
print(len(ans))

