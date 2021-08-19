N = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a_max = 0
c_max = 0
c = [0]

for i in range(N):
    a_max = max(a[i],a_max)
    c_max = max(c[i],c_max)
    c.append(max(a_max*b[i],c_max))
    
for i in range(1,N+1):
    print(c[i])