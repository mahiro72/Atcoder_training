from collections import deque
N,M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A = deque(A)
B = deque(B)

C = []
while A or B:
    if A and B:
        if A[0]<=B[0]:
            a = A.popleft()
            C.append(a)
        else:
            b = B.popleft()
            C.append(b)
    elif A:
        a = A.popleft()
        C.append(a)
    else:
        b = B.popleft()
        C.append(b)

print(*C,sep="\n")