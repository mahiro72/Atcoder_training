from math import gcd

def prime(x):
    a = set()
    while x%2==0:
        x//=2
        a.add(2)
    f = 3
    while f*f<=x:
        if x%f==0:
            x//=f
            a.add(f)
        else:
            f+=2
    if x!=1:
        a.add(x)
    return a
        

N = int(input())
A = list(map(int,input().split()))


ch = set()

pairwise = True
setwise = True

for i,a in enumerate(A):
    if i==0:
        ch |= prime(a)
    else:
        tmp = prime(a)
        if len(ch&tmp)>0:
            pairwise = False
            break
        else:
            ch |= tmp

p = A[0]
for i,a in enumerate(A):
    if i==0:continue
    p = gcd(p,a)

if p>1:
    setwise = False

    
if pairwise:
    print('pairwise coprime')
elif setwise:
    print('setwise coprime')
else:
    print('not coprime')
