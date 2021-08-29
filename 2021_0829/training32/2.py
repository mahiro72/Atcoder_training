A,B,C =map(int,input().split())

s = A
while s%B!=0:
    s+=A
s+=A

while s%B!=0:
    if s%B==C:
        exit(print('YES'))
    s+=A
print('NO')
