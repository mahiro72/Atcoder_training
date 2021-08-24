from math import gcd

N = int(input())
A = list(map(int,input().split()))

l,r = [A[0]],[A[-1]]

for i in range(1,N):
    l.append(gcd(l[-1],A[i]))
    r.append(gcd(r[-1],A[-i-1]))

# ans=max(l[-2],r[-2])
# if N>2:
#     for i in range(N-2):
#         ans=max(ans,gcd(l[i],r[N-i-3]))
#  

# print(ans)

r = r[::-1]
ans = 0
for i in range(N):
    if i==0:
        ans = max(ans,r[i+1])
    elif i==N-1:
        ans = max(ans,l[i-1])
    else:
        ans = max(ans,gcd(l[i-1],r[i+1]))
print(ans)

