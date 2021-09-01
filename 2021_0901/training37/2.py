N,X,M = map(int,input().split())

def f(a,m):
    return a**2%m


a = X
now = 0
num = [0]*(10**5+1)
loop_start,loop_fin = 0,0

while True:
    now+=1
    if num[a]==0:
        num[a]=now
    else:
        loop_start = num[a]
        loop_fin = now-1
        break
    a = f(a,M)


loop = loop_fin-loop_start+1
ans = 0
a = X

for i in range(loop_start-1):
    ans += a
    a = f(a,M)
    N-=1

loop_sum = []

for i in range(loop):
    loop_sum.append(a)
    a = f(a,M)

ans += sum(loop_sum)*(max(0,N)//loop)+sum(loop_sum[:max(0,N)%loop])
print(ans)