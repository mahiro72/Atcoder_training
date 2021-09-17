from collections import Counter

N = int(input())
A = list(map(int,input().split()))

cum = [0]
for i in range(N):
    cum.append(cum[i]+A[i])

ans = 0
c = Counter(cum)
for _,cnt in c.items():
    if cnt>=2:
        ans+= cnt*(cnt-1)//2

print(ans)
