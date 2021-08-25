R,G,B,N = map(int,input().split())

ans = 0
for r in range(N//R+1):
    for g in range(N//G+1):
        if (N-(R*r+G*g))>=0 and (N-(R*r+G*g))%B==0:
            ans+=1
print(ans)
