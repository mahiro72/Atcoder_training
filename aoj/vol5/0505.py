
def f():
    N,M = map(int,input().split())
    x = [list(map(int,input().split()))for _ in range(N)]
    num = [[0,x]for x in range(1,M+1)]
    for i in range(M):
        for j in range(N):
            num[i][0]+=x[i][j]
    num.sort(reverse=True)
    re = [i[1] for i in num]
    return re

r = f()
print(r)