N = int(input())
X = list(map(int,input().split()))

X2 = sorted(X)
mid1,mid2 = X2[N//2-1],X2[N//2]

for x in X:
    if x<=mid1:
        print(mid2)
    else:
        print(mid1)