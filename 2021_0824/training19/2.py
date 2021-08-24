S = input()
atcg = "ATCG"
cnt,ans=0,0
for i in S:
    if i in atcg:
        cnt+=1
        ans = max(ans,cnt)
    else:
        cnt=0
print(ans)