N, K = map(int, input().split())

ans = 0
for b in range(K+1, N+1):
    ans += (b-K)*(N//b) + max(0, N-(N//b)*b-K+1)
if K == 0:
    print(N*N)
else:
    print(ans)
