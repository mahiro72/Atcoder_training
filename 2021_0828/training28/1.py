N =int(input())
a = list(int(input())-1 for _ in range(N))

nxt,ans = 0,0
used = [False]*N

while used[nxt]==False:
    used[nxt]=True
    nxt = a[nxt]
    ans +=1 
    if nxt==1:
        used[nxt]=True
        break

if used[1]==True:
    print(ans)
else:
    print(-1)