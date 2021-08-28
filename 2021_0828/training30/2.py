N = int(input())
P = list(map(int,input().split()))

ans = 0
flg = True
for i,p in enumerate(P):
    if p==i+1 and flg:
        ans+=1
        flg = False
    else:
        flg = True

print(ans)
