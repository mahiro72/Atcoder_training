A,B,C = map(int,input().split())

cnt = 0
pre = 0

while A%2==0 and B%2==0 and C%2==0:
    cnt+=1
    temp1 = A
    A = B//2+C//2
    temp2 = B
    B = temp1//2+C//2
    C = temp1//2+temp2//2
    if pre == abs(A-B):
        cnt=-1
        break
    pre = abs(A-B)
    
print(cnt)
