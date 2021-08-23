N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

if sum(A)>sum(B):
    print("No")
else:
    a,b=0,0
    for i in range(N):
        if A[i]>B[i]:
            a+= A[i]-B[i]
        else:
            b+=(B[i]-A[i])//2
    if b>=a:
        print("Yes")
    else:
        print("No")