# https://atcoder.jp/contests/abc136/tasks/abc136_d

import math
S = input()
l = [0]*len(S)

cnt_r = 1
cnt_l = 0

i = 0
while i+1<len(S):
    if S[i]=="R" and S[i+1]=="L":
        now = i
        while now+1<len(S) and S[now+1]=="L":
            now+=1
            cnt_l += 1

        l[i]=math.ceil(cnt_r/2)+cnt_l//2
        l[i+1]=math.ceil(cnt_l/2)+cnt_r//2
        cnt_r = 0
        cnt_l = 0

        i=now
    else:
        cnt_r+=1
        i+=1
print(*l)

