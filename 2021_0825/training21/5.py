N,M,K = map(int,input().split())

if N==K or M==K:
    print("Yes")
else:
    for x in range(M+1):
        for y in range(N+1):
            if x*y+(M-x)*(N-y)==K:
                exit(print("Yes"))
    print("No")
