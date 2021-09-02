S = input()+'0'
N = len(S)

mod = 2019
cnt = [0]*mod
cnt[0] = 1
tmp = 0

for i in range(1,N):
    tmp = (tmp+int(S[N-i-1])*(pow(10,(i-1),mod)))%mod
    cnt[tmp] += 1

print(sum([(c*(c-1))//2 for c in cnt]))