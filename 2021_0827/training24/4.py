N = int(input())
ab = sorted([list(map(int,input().split()))for _ in range(N)])
cd = sorted([list(map(int,input().split()))for _ in range(N)])
ans = 0
for c,d in cd:
    r = [[a,b]for a,b in ab if a<c and b<d]
    if r:
        r.sort(key=lambda x:x[1])
        ab.remove(r[-1])
        ans+=1
print(ans)
