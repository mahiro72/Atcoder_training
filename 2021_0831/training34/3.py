N,M= map(int,input().split())

s = [pow(2,i)for i in range(12)]
INF = 10**18
dp = [[INF]*pow(2,N)for _ in range(M+1)]
dp[0][0] = 0

for i in range(M):
    a,b = map(int,input().split())
    X = sum([s[i-1]for i in list(map(int,input().split()))])

    for j in range(pow(2,N)):
        dp[i+1][j] = min(dp[i+1][j],dp[i][j])
        dp[i+1][j|X] = min(dp[i+1][j|X],dp[i][j|X],dp[i][j]+a)

ans = dp[-1][-1]
print(ans if ans!=INF else -1)



























# N,M = map(int,input().split())

# ab = []
# C = []

# for i in range(M):
#     a,b = map(int,input().split())
#     c = list(map(int,input().split()))
#     ab.append((a,b))
#     C.append(c)

# dp = [[float('inf')]*N for _ in range(M+1)]

# for i in range(1,M+1):
#     a,b = ab[i-1]
#     for j in range(N):
#         dp[i][j] = min(dp[i][j],dp[i-1][j])

#     for j,c in enumerate(C[i-1]):
#         dp[i][c-1] = min(dp[i-1][c-1],a)


# ans = sum(list(set(dp[-1])))
# print(ans if ans!=float('inf') else -1)
