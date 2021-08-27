N,K,S = map(int,input().split())
x = [S for _ in range(K)]
if S==10**9:
    x += [1 for _ in range(N-K)]
else:
    x += [S+1 for _ in range(N-K)]
print(*x)