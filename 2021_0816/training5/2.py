# https://atcoder.jp/contests/abc088/tasks/abc088_c

C = list(list(map(int,input().split()))for _ in range(3))

for a1 in range(101):
    b = list(map(lambda x:x-a1,C[0]))
    if min(b)<0:
        continue
    cnt = 0
    for i in range(1,3):
        temp_a = []
        for j in range(3):
            if C[i][j]>=b[j]:
                temp_a.append(C[i][j]-b[j])
        if len(temp_a)==3 and (temp_a[0]==temp_a[1]==temp_a[2]):
            cnt+=1
    if cnt==2:
        exit(print("Yes"))

print("No")
