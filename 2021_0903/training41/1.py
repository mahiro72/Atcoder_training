from math import gcd
N,K = map(int,input().split())
A = list(map(int,input().split()))

if K in set(A):
    exit(print('POSSIBLE'))
elif max(A)<K:
    exit(print('IMPOSSIBLE'))
else:
    tmp = A[0]
    for i in range(1,N):
        tmp = gcd(tmp,A[i])
    if K%tmp==0:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')