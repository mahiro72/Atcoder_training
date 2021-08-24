n,k = map(int,input().split())
ans = 0
for i in range(2,2*n+1):
    if i-k >= 2 and i-k <= 2*n:
        ans += min(i-1,2*n+1-i) * min(i-k-1,2*n+1-(i-k))
print(ans)
