from collections import Counter
N,M = map(int,input().split())
A = list(map(int,input().split()))
c = sorted(Counter(A).values(),reverse=True)
print(c[0])