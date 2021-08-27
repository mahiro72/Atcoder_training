N,K = map(int,input().split())
S = input()

for _ in range(K):
    T = ""
    for i in range(0,2*N,2):
        s1 = S[i%N]
        s2 = S[(i+1)%N]
        if s1==s2:
            T+=s1
        elif (s1,s2) in (("R","S"),("S","R")):
            T+="R"
        elif (s1,s2) in (("P","S"),("S","P")):
            T+="S"
        else:
            T+="P"
    S = T
print(S[0])