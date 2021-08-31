N,K = map(int,input().split())
X,Y = [],[]
XY = []
for i in range(N):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)
    XY .append((x,y))

X.sort()
Y.sort()
INF = float('inf')

ans = INF
for i in range(N-1):
    for j in range(i+1,N):
        for k in range(N-1):
            for l in range(k+1,N):
                tmp = 0
                for x,y in XY:
                    if X[i]<=x<=X[j] and Y[k]<=y<=Y[l]:
                        tmp+=1
                if tmp>=K:
                    ans = min(ans,(X[j]-X[i])*(Y[l]-Y[k]))
print(ans)