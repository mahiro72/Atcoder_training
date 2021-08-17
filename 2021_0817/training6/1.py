# https://atcoder.jp/contests/hhkb2020/tasks/hhkb2020_c

N = int(input())
P = list(map(int,input().split()))

l = [0]*(2*10**5+1)
now = 0
for i in range(N):
    l[P[i]] =1 
    while l[now]==1:
        now+=1
    print(now)
