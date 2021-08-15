N = int(input())
S = input()
T = input()
ans = N*2
for i in range(N):
    if S[(N-i-1):]==T[:(i+1)]:
        ans = min(ans,N*2-i-1)
print(ans)
