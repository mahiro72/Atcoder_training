import bisect

N,Q = map(int,input().split())
A = list(map(int,input().split()))
K = list(int(input())for _ in range(Q))

# A 以下の良い整数の個数 C を記録
C = list(A[i]-(i+1) for i in range(N))

for k in K:
    if C[-1]<k:
        print(A[-1]+(k-C[-1]))
    else:
        tmp = bisect.bisect_left(C,k)
        print(A[tmp]-C[tmp]+k-1)