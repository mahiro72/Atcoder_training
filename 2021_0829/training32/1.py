N = int(input())
A = list(int(input())for _ in range(N))
d = {x:0 for x in set(A)}

for a in A:
    d[a]+=1

ans = 0
for _,value in d.items():
    if value%2:
        ans+=1

print(ans)