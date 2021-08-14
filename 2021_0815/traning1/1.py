N = int(input())
A = sorted(list(map(int,input().split())))
for i,a in enumerate(A):
    if i+1!=a:
        exit(print("No"))
print("Yes")