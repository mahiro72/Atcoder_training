from itertools import combinations
N = int(input())
L = list(map(int,input().split()))

cnt=0
for a,b,c in combinations(L,3):
    if a+b>c and a+c>b and c+b>a:
        if a!=b and b!=c and c!=a:
            cnt+=1
print(cnt)