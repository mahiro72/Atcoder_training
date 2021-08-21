import bisect

N,M,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.append(0)

ruiB = [0]
for i in range(M):
    ruiB.append(ruiB[i]+B[i])

ans =0
for i in range(N+1):
    if i>0:
        K-=A[i-1]
    if K<0:
        break
    temp = bisect.bisect_right(ruiB,K)-1
    ans = max(ans,i+temp)
print(ans)
