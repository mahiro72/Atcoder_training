N = int(input())
A = [int(input())for _ in range(N)]
A.sort()

if N%2==0:
    A1 = A[0:N//2]
    A2 = A[N//2:]
    ans = (2*sum(A2)-A2[0])-(2*sum(A1)-A1[-1])
else:
    A1 = A[0:N//2]
    A2 = A[N//2+1:]
    ans = (2*sum(A2)-A2[0])-(2*sum(A1)-A1[-1])
    ans += max(abs(A[N//2]-A1[-1]),abs(A[N//2]-A2[0]))

print(ans)