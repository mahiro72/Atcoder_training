from math import comb
A,B,K = map(int,input().split())

ans = ""
while A>0 and B>0:
    a_comb = comb(A-1+B,A-1)
    if a_comb>=K:
        ans+="a"
        A-=1
    else:
        ans+="b"
        B-=1
        K-=a_comb

ans+='a'*A+"b"*B
print(ans)
        
