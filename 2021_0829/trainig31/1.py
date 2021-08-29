N,M = map(int,input().split())
S,T = (list(map(int,input().split()))for _ in range(2))
now,ans = 0,0

for t in T:
    for i in range(N//2+1):
        if S[now-i]==t:
            ans += (i+1)
            now -= i
            break
        elif S[now%N+i]==t:
            ans += (i+1)
            now += i
            break
        if i==N//2:
            exit(print(-1))
print(ans)
