N = int(input())
S = input()
T = input()

A,B = ([0 for _ in range(500000)]for _ in range(2))
cnt_a ,cnt_b =0,0
ans = 0

for i in range(N):
    if S[i]=='0':
        A[cnt_a] = i
        cnt_a+=1
    if T[i]=='0':
        B[cnt_b] = i
        cnt_b+=1

if cnt_a!=cnt_b:
    print(-1)
else:
    for a,b in zip(A,B):
        if a!=b:
            ans+=1
    print(ans)
