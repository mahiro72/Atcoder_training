A,B,C,K = map(int,input().split())


pre = A-B
now = 0

while now<K:
    now += 1
    tempA = A 
    tempB = B
    A = B+C
    B = tempA+C
    C = tempA+tempB
    if abs(pre)==abs(A-B):
        pre = A-B
        if (K-now)%2:
            pre*=-1
        break
    pre = A-B

if abs(A-B)>10**18:
    print("Unfair")
else:
    print(pre)
