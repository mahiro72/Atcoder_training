N = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

a_max,c_max = 0,0
c = []
for a,b in zip(a,b):
    a_max = max(a_max,a)
    c_max = max(c_max,a_max*b)
    c.append(c_max)
print(*c,sep="\n")
