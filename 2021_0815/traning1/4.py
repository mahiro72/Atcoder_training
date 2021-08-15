N = int(input())
T = list(map(int, input().split()))

total = sum(T)

# dp[i][t] := i番目まで料理作成が終わっていて、オーブンAの使用時間がtであるときのオーブンBの使用時間の最小値
dp = [[float("inf")] * (total+1) for _ in range(N+1)]
dp[0][0] = 0

for i in range(N):
    for t in range(total):
        if dp[i][t] != float("inf"):
            dp[i + 1][t + T[i]] = min(dp[i + 1][t + T[i]], dp[i][t])
            dp[i + 1][t] = min(dp[i + 1][t], dp[i][t] + T[i])

ans = float("inf")
for t in range(total):
    ans = min(ans, max(t, dp[N][t]))

print(ans)
