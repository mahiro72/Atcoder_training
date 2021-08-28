H,W = map(int,input().split())
S = [input()for _ in range(H)]

left = [[0]*W for _ in range(H)] #左から
right = [[0]*W for _ in range(H)]
up = [[0]*W for _ in range(H)] 
down = [[0]*W for _ in range(H)]

for i in range(H):
    cnt = 0
    for j in range(W):
        if S[i][j]=='.':
            cnt+=1
        else:
            cnt=0
        left[i][j] = cnt


for i in range(H):
    cnt = 0
    for j in range(W-1,-1,-1):
        if S[i][j]=='.':
            cnt+=1
        else:
            cnt=0
        right[i][j] = cnt


for i in range(W):
    cnt = 0
    for j in range(H):
        if S[j][i]=='.':
            cnt +=1
        else:
            cnt = 0
        up[j][i] = cnt



for i in range(W):
    cnt = 0
    for j in range(H-1,-1,-1):
        if S[j][i]=='.':
            cnt +=1
        else:
            cnt = 0
        down[j][i] = cnt

ans = 0
for i in range(H):
    for j in range(W):
        cnt = left[i][j]+right[i][j]+up[i][j]+down[i][j]-3
        ans = max(ans,cnt)

print(ans)