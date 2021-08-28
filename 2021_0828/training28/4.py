X,Y,A,B,C = map(int,input().split())
p = sorted(list(map(int,input().split())),reverse = True)
q = sorted(list(map(int,input().split())),reverse = True)
r = sorted(list(map(int,input().split())))

temp = p[:X]+q[:Y]
temp.sort()
ans = 0
for i in range(X+Y):
    if r and temp[i]<r[-1]:
        ans+=r[-1]
        r.pop()
    else:
        ans+=temp[i]

print(ans)
