N = int(input())
a = list(map(int,input().split()))

cnt=0
cnt2=-1
for i in range(N):
    if a[i]%4==0:
        cnt+=2
    elif a[i]%2==0:
        cnt2+=1

if N-1<=(cnt+max(cnt2,0)):
    print("Yes")
else:
    print("No")
