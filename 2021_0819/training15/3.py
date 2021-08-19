from itertools import groupby

S = input()[::-1]

dic = {x:0 for x in "abcdefghijklmnopqrstuvwxyz"}

now = 0
ans = 0
for alpha,l in groupby(S):
    cnt = len(list(l))
    if cnt>=2:
        ans+=now-dic[alpha]
        dic = {x:0 for x in "abcdefghijklmnopqrstuvwxyz"}
        now+=cnt
        dic[alpha]=now
    else:
        now+=cnt
        dic[alpha]+=cnt

print(ans)