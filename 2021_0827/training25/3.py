N,x = map(int,input().split())
a = list(map(int,input().split()))

ans = 0
for i in range(1,N):
    if a[i]+a[i-1]>x:
        ans+=a[i]-(x-a[i-1])
        a[i] = max(0,x-a[i-1])

print(ans)