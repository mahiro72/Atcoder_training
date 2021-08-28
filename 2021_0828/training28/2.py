N,K,S = map(int,input().split())

if S==10**9:
    print(*([S for _ in range(K)]+[1 for _ in range(N-K)]))
else:
    print(*([S for _ in range(K)]+[S+1 for _ in range(N-K)]))
