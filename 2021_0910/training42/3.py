N, C = map(int, input().split())
D = [list(map(int, input().split())) for i in range(C)]
c = [list(map(int, input().split())) for i in range(N)]
col = [[0]*C for i in range(3)]
for i in range(N):
    ci = c[i]
    for j in range(N):
        cc = col[(i+j)%3]
        dd = D[ci[j]-1]
        for k in range(C):
            cc[k] += dd[k]
ans = 10**18
c0 = col[0]
c1 = col[1]
c2 = col[2]
for i in range(C):
    for j in range(C):
        if i == j:
            continue
        for k in range(C):
            if i == k or j == k:
                continue
            ans = min(ans, c0[i] + c1[j] + c2[k])
print(ans)