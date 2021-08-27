N = int(input())
A = list(map(int,input().split()))
A.sort(reverse=True)

ans = 1
mod = 10**9+7

for i in range(1,N):
    ans*=(A[i-1]-A[i]+1)%mod
print(ans*(A[-1]+1)%mod)