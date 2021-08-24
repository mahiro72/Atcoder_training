N = int(input())
T = list(map(int,input().split()))
M = int(input())

sum_t = sum(T)
ans = []

for i in range(M):
    P,X = map(int,input().split())
    ans.append(sum_t-T[P-1]+X)

print(*ans,sep="\n")