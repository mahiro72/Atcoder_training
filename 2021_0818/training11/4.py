S = input()
ans = 0
for i in range(2**(len(S)-1)):
    temp = [0]*(len(S)-1)
    for j in range(len(S)-1):
        if (i>>j)&1:
            temp[j]=1
    l = []
    now = 0
    for a in range(len(S)-1):
        if temp[a]==1:
            l.append("".join(S[now:a+1]))
            now = a+1
    l.append(S[now:])
    l = list(map(int,l))
    ans += sum(l)
print(ans)



    