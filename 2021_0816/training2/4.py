N,K = map(int,input().split())

if K==0:
    exit(print(N*N))

ans = 0
for b in range(K+1,N+1):
    ans += (N//b)*max(0,b-K)+max(0,N%b-K+1)
print(ans)
