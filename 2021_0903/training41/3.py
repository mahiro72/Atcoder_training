n = int(input())
mod = 10**9 +7

dp = [[[[0]*4 for _ in range(4)] for _ in range(4)] for _ in range(n+1)]
dp[0][0][0][0]=1
#T:0,A:1,G:2,C:3

for l in range(n):
    for c3 in range(4):
        for c2 in range(4):
            for c1 in range(4):
                if dp[l][c3][c2][c1]==0:continue
                for c0 in range(4):
                    if c2 == 1 and c1 == 2 and c0 == 3:continue
                    if c2 == 2 and c1 == 1 and c0 == 3:continue
                    if c2 == 1 and c1 == 3 and c0 == 2:continue
                    if c3 == 1 and c1 == 2 and c0 == 3:continue
                    if c3 == 1 and c2 == 2 and c0 == 3:continue
                    dp[l+1][c2][c1][c0]+=dp[l][c3][c2][c1]
                    dp[l+1][c2][c1][c0]%=mod

ans = 0
for c3 in range(4):
        for c2 in range(4):
            for c1 in range(4):
                ans+= dp[n][c3][c2][c1]
                ans %= mod

print(ans)
