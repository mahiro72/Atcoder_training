N,K = map(int,input().split())

low,high=0,0
mod = 10**9+7
ans = 0

for k in range(1,N+2):
    low += k-1
    high += N-k+1
    if k>=K:
        ans+=(high-low+1)%mod

print(ans%mod)