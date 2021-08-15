S = input()
w = int(input())

ans=""
for i,s in enumerate(S):
    if i%w==0:
        ans+=s
print(ans)
