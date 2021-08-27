N,M = map(int,input().split())
even,odd = 0,0

for i in range(N):
    s = input().count("1")
    if s%2:
        odd+=1
    else:
        even+=1
print(odd*even)