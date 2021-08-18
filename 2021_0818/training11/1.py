A1,A2,A3 = map(int,input().split())

if abs(A1-A3)%2:
    if A2<=(A1+A3)//2:
        ans = (A1+A3+1)//2-A2+1
    else:
        ans = A2*2-(A1+A3)
else:
    if A2<=(A1+A3)//2:
        ans = (A1+A3)//2-A2
    else:
        ans = A2*2-(A1+A3)
print(ans)