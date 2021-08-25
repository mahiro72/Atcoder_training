N,K = map(int,input().split())
a = list(map(int,input().split()))

l = [0]*(max(a)+2)
for i in a:
    l[i]+=1
print(l)
ans = 0
for i in range(len(l)):
    if l[i]<K:
        ans+= i*(K-l[i])
        K = l[i]
print(ans)