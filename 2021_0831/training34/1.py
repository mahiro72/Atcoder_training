N,M = map(int,input().split())
A = list(map(int,input().split()))

memo = [0]*(N+1)

for a in A[:M]:
    memo[a]+=1

ans = memo.index(0)

for i in range(N-M):
    memo[A[i+M]]+=1
    memo[A[i]]-=1
    if memo[A[i]] == 0:
        ans = min(ans,A[i])

print(ans)








# memo = [0]*(N+1)

# for i in range(M):
#     memo[A[i]] += 1


# ans = [memo.index(0)]

# for i in range(1,N-M+1):
#     memo[A[i-1]]-=1
#     memo[A[i+M-1]]+=1
#     ans.append(memo.index(0))

# print(min(ans))
