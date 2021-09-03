N = int(input())
A = list(map(int,input().split()))
A.sort()
cum = [0]
for i in range(N):
    cum.append(A[i]+cum[i])

ans = 1
for i in range(1,N):
    if 2*cum[i]>=A[i]:
        ans +=1
    else:
        ans = 1

print(ans)
