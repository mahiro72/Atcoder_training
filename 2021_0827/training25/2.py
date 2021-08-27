N = int(input())
ab = []
for _ in range(N):
    a,b = map(int,input().split())
    ab.append([a,b])

ans = 0
for a,b in ab[::-1]:
    a += ans
    amari = a%b
    if amari!=0:
        ans+=b-amari
print(ans)