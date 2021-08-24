N = int(input())
f = [0]*(N+1)

for x in range(1,int(N**0.5)+1):
    for y in range(1,int(N**0.5)+1):
        for z in range(1,int(N**0.5)+1):
            n = x**2+y**2+z**2+x*y+y*z+z*x
            if n<=N:
                f[n]+=1
            else:
                break

print(*f[1:],sep="\n")
