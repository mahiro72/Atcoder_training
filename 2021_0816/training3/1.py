N,K = map(int,input().split())

s = set()
for i in range(K):
    d = int(input())
    A = set(map(int,input().split()))
    s |= A

sunuke = set(i for i in range(1,N+1))

ans = 0
for i in sunuke:
    if i not in s:
        ans+=1
print(ans)
