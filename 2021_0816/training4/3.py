# https://atcoder.jp/contests/agc016/tasks/agc016_a
S = input()
m = S[0]
cnt = 1
l = []
for i in range(1,len(S)+1):
    if i==len(S):
        l.append((m,cnt))
    elif S[i]!=m:
        l.append((m,cnt))
        m = S[i]
        cnt = 1
    else:
        cnt+=1

ans = len(S)
for s in set(S):
    length = 0
    temp = 0
    for m,cnt in l:
        if m!=s:
            length+=cnt
        else:
            temp = max(temp,length)
            length=0
    temp = max(temp,length)
    ans = min(ans,temp)

print(ans)