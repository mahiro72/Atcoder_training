N = int(input())

def check(x):
    return x*(x+1)//2<=N+1

def f(l,r):
    while l<=r:
        mid = (l+r)//2
        if check(mid):
            l = mid+1
        else:
            r = mid-1
    return r

k = f(0,N+1)
print(min(N,N-k+1))
