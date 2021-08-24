a,b,x,y = map(int,input().split())

mi = min(2*x,y)
if a==b:
    print(x)
elif b>a:
    print(mi*(b-a)+x)
else:
    print(mi*(a-b-1)+x)
