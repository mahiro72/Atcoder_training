N = int(input())
C = [int(input())for _ in range(N)]

color = [-1]*(2*10**5+1)
dp = [0]*(N+1)
dp[0]=1
mod = 10**9+7

for i in range(1,N+1):
    c = C[i-1]
    if color[c]==i-1 or color[c]==-1:
        dp[i] += dp[i-1]%mod
    else:
        dp[i] += (dp[i-1]+dp[color[c]])%mod
    color[c] = i

print(dp[N]%mod)
