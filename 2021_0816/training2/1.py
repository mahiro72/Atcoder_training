n = int(input())
p = list(map(int,input().split()))

cnt=0
for i in range(2,n):
    if p[i-2]<p[i-1]<p[i] or p[i-2]>p[i-1]>p[i]:
        cnt+=1
print(cnt)
