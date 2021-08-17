# https://atcoder.jp/contests/abc094/tasks/arc095_a

N = int(input())
X = list(map(int,input().split()))
X2 = sorted(X)
mid1 = X2[N//2-1]
mid2 = X2[N//2]

if mid1==mid2:
    print(*([mid1]*N),sep="\n")
else:
    for i in range(N):
        if X[i]<=mid1:
            print(mid2)
        if X[i]>=mid2:
            print(mid1)