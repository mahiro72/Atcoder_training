N,A,B = map(int,input().split())

if A>B:
    print(0)
else:
    if N==1:
        if A==B:
            print(1)
        else:
            print(0)
    elif N==2:
        print(1)
    else:
        print(((N-1)*B+A)-((N-1)*A+B)+1)