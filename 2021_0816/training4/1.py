# https://atcoder.jp/contests/agc027/tasks/agc027_a

N,x = map(int,input().split())
A = sorted(list(map(int,input().split())))

ans = 0
ch=True
for a in A:
    if a<=x:
        x-=a
        ans+=1
    else:
        ch=False
        break
if x>0 and ch:
    ans-=1

print(ans)