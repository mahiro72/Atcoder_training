N = int(input())

if N%2:
    print(0)
else:
    ans = 0
    i = 1
    while N//2 >= 5**i:
        ans += (N//2)//5**i
        i+=1
    print(ans)
