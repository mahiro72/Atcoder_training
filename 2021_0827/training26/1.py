from collections import Counter

N,K = map(int,input().split())
A = list(map(int,input().split()))
k = len(set(A))

if K>=k:
    exit(print(0))
ans = 0
for i in sorted(Counter(A).values()):
    ans+=i
    k-=1
    if K>=k:
        break
print(ans)
