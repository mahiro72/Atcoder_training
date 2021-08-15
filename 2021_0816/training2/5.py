A,B = map(int,input().split())

def f(x):
    if x%2==1:
        if (x+1)%4==0:
            return 0
        else:
            return 1
    else:
        return f(x+1)^(x+1)

print(f(A-1)^f(B))

