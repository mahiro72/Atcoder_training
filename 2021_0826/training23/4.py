N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

if sum(A)<sum(B):
    print(-1)
else:
    ch = True
    m,z,p = [],[],[]
    for a,b in zip(A,B):
        if b-a==0:
            z.append(b-a)
        elif b-a>0:
            p.append(b-a)
        else:
            m.append(b-a)
    temp = sorted(p,reverse=True)+z+sorted(m)
    ans = 0

    if sum(p)==0:
        exit(print(0))

    for i in range(N):
        ans+=temp[i]
        if ans<0:
            exit(print(i+1))