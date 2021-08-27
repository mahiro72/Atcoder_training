
n=int(input())
a=list(map(int,input().split()))
a.sort()
ans=0
mod=998244353
su=a[0]
for i in range(1,n):
  ans=(ans+su*a[i])%mod
  su=(su*2+a[i])%mod
for i in range(n):
  ans+=a[i]*a[i]
print(ans%mod)
