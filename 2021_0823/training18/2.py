# N = int(input())

# s = set()
# num = []
# for i in range(N):
#     S,P = map(str,input().split())
#     s.add(S)
#     num.append((S,int(P)))

# d = {x:[] for x in s}
# for i in range(N):
#     d[num[i][0]].append(num[i][1])

# for i in sorted(list(d.keys())):
#     for j in sorted(d[i],reverse=True):
#         print(num.index((i,j))+1)

N = int(input())
ans = []
for i in range(N):
    S,P = input().split()
    ans.append((S,-int(P),i+1))

ans.sort()
for _,_,a in ans:
    print(a)
