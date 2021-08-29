N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

d = {x:0 for x in set(A)}
for a in A:
    d[a]+=1

ans = []
a_list = set(A)

for a in A:
    flag = True
    x = 0
    tmp_dic = d.copy()
    for i,b in enumerate(B):
        if i==0:
            x = a^b
        else:
            tmp_a = x^b
            if tmp_a in a_list and  tmp_dic[tmp_a]>0:
                tmp_dic[tmp_a]-=1
            else:
                flag = False
                break
    if flag:
        ans.append(x)

print(len(ans))
print(*sorted(ans),sep='\n')
