a,b,x = map(int,input().split())
import math

def f(up):
    return (up+b)*a/2*a

def solve(l,r):
    while l+pow(10,-6)<r:
        c1=l+(r-l)/3
        c2=r-(r-l)/3
        if f(c1)<f(c2):
            r=c2
        else:
            l=c1
    return l

print(math.degrees(math.atan((b-solve(0,b))/a)))
