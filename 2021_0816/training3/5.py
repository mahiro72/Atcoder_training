N = int(input())
A = list(map(int,input().split()))
# d = N-len(set(A))
# cnt=(d+1)//2
# print(N-cnt*2)
K = len(set(A))
if K%2==1:
    print(K)
else:
    print(K-1)
