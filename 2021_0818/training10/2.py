N = int(input())
A = list(map(int,input().split()))

from collections import Counter

c = Counter(A)
ans = 0
for k,v in c.items():
    if k>v:
        ans += v
    elif k<v:
        ans += (v-k)

print(ans)
