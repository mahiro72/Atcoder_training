# https://atcoder.jp/contests/abc075/tasks/abc075_b

H,W = map(int,input().split())
S = [list(x for x in input()) for _ in range(H)]

dwh = [(0,1),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(1,0),(1,1)]
for h in range(H):
    for w in range(W):
        cnt=0
        if S[h][w]=="#":
            continue
        for dw,dh in dwh:
            if 0<=w+dw<W and 0<=h+dh<H:
                if S[h+dh][w+dw]=="#":
                    cnt+=1
        S[h][w] = str(cnt)
    

for i in S:
    print(''.join(i))
