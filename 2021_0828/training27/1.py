N,K = map(int,input().split())

ans = 0
for i in range(1,N+1):
    cnt = 0
    while K>i:
        i*=2
        cnt+=1
    ans += pow(1/2,cnt)
print(ans/N)