N,K = map(int,input().split())

if K==0:exit(print(N**2))

ans,cnt = 0,1
for b in range(K+1,N+1):
    ans += (N+1)//b*cnt + max(0,(N+1)%b-K)
    cnt+=1

print(ans)