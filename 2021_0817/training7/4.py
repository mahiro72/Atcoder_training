
import itertools
N = int(input())
S = list(input())
T = input()
mod = 10**9+7
G = itertools.groupby(S)
L = []

for k,g in G:
    L.append(len(list(g)))

ans = 3*L[0]
for i in range(len(L)-1):
    if L[i]==1 and L[i+1]==1:
        ans*=2
    if L[i]==2 and L[i+1]==2:
        ans*=3
    if L[i]==1 and L[i+1]==2:
        ans*=2
 
print(ans%mod)