H,W,A,B = map(int,input().split())

ans = []
for i in range(H):
    temp = ""
    for j in range(W):
        if i<B and j<A:
            temp+='0'
        elif i>=B and j>=A:
            temp+='0'
        else:
            temp+='1'
    ans.append(temp)

print(*ans,sep="\n")
