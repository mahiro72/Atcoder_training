N,M = map(int,input().split())

ab = [tuple(map(int,input().split()))for _ in range(M)]
ab.sort(key=lambda x:x[1])

pre_b = -1
nxt_a = -1
cnt = 0

for a,b in ab:
    nxt_a = a
    if pre_b<=nxt_a:
        cnt+=1
        pre_b=b
print(cnt)