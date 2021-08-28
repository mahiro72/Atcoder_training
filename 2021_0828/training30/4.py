N = int(input())

s,i = 0,1
while s<N:
    s += i
    i+=1

dif = s-N
for i in range(1,i):
    if i!=dif:
        print(i)
