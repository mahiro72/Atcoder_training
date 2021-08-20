N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]

ans = 0
ansx,ansy=-1,-1

for cy in range(101):
    for cx in range(101):
        ch=True
        for i,(x,y,h) in enumerate(data):
            if h!=0:
                h_temp = h+abs(x-cx)+abs(y-cy)
                break

        for i,(x,y,h) in enumerate(data):
            if h!=max(h_temp-abs(x-cx)-abs(y-cy),0):
                ch=False
                break
        if ch:
            exit(print(cx,cy,h_temp))

