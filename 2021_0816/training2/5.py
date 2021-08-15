A,B = map(int,input().split())

ans = A
for i in range(A+1,B+1):
    ans ^=i

print(ans)
