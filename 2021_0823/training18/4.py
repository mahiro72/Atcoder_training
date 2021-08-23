A,B,W = map(int,input().split())

mi = float("inf")
ma = 0
s,g = W*1000//B,W*1000//A+1
for i in range(s,g):
    if A*i<=1000*W<=B*i:
        mi = min(mi,i)
        ma = max(ma,i)
if ma==0:
    print("UNSATISFIABLE")
else:
    print(mi,ma)
    
