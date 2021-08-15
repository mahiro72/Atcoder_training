import math
A,B,N = map(int,input().split())
def f(x):
    return math.floor(A*x/B)-(A*math.floor(x/B))
print(f(min(N,B-1)))