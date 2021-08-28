N = int(input())
A = list(map(int,input().split()))
cnt = [0]*(10**5+1)

for a in A:
    cnt[a]+=1

ans = 0
for i in range(len(cnt)):
    if i==0:
        ans = max(ans,cnt[i]+cnt[i+1])
    elif i==len(cnt)-1:
        ans = max(ans,cnt[i]+cnt[i-1])
    else:
        ans = max(ans,cnt[i-1]+cnt[i]+cnt[i+1])

print(ans)
