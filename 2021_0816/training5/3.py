# https://atcoder.jp/contests/nikkei2019-2-qual/tasks/nikkei2019_2_qual_b

from collections import Counter
N = int(input())
D = list(map(int,input().split()))
counter = Counter(D)
mod = 998244353

if counter[0]!=1 or D[0]!=0:
    exit(print(0))

ans = 1
for i in range(1,max(D)+1):
    ans *= pow(counter[i-1],counter[i],mod)
print(ans%mod)
