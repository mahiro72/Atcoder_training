from itertools import groupby

S = input()[::-1]
ans,now = 0,0
alpha = "abcdefghijklmnopqrstuvwxyz"
d = {x:0 for x in alpha}

for i,l in groupby(S):
    l = len(list(l))
    if l>=2:
        ans+=(now-d[i])
        d = {x:0 for x in alpha}
        now += l
        d[i]+= now
    else:
        now += l
        d[i]+= l
    
print(ans)
