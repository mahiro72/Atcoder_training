N = int(input())
data = [[]for _ in range(N)]

for i in range(N):
    a = int(input())
    for j in range(a):
        x,y = map(int,input().split())
        data[i].append((x-1,y))

ans = 0
for i in range(2**N):
    people = [0]*(N)
    for j in range(N):
        if (i>>j)&1:
            people[j]=1
    cnt = 0
    for x in range(N):
        ch=False
        if people[x]==1:
            ch=True
            for p,b in data[x]:
                if people[p]!=b:
                    cnt += -float("inf")
        if ch:
            cnt+=1   
    ans = max(ans,cnt)

print(ans)