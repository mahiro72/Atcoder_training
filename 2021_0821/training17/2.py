from collections import Counter

N,P = map(int,input().split())

def f(x):
    re = []
    while x%2==0:
        x//=2
        re.append(2)
    mod = 3
    while mod*mod<=x:
        if x%mod==0:
            re.append(mod)
            x//=mod
        else:
            mod+=2
    if x!=1:
        re.append(x)
    return re

c = Counter(f(P))
ans = 1
for key,value in c.items():
    if value>=N:
        ans*=key**(value//N)

print(ans)