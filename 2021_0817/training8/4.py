N = int(input())
A = list(map(int,input().split()))
l = len(set(A))
if l%2==1:
    print(l)
else:
    print(l-1)