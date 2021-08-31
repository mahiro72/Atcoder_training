N = int(input())
A = list(map(int,input().split()))

mod = 1000000007
ans = 1
r,g,b = 0,0,0

for i in A:
    ans*=[r,g,b].count(i)%mod
    if r==i:r+=1
    elif g==i:g+=1
    elif b==i:b+=1
    else:exit(print(0))

print(ans%mod)

