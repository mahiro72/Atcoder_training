
N, K = map(int, input().split())
mod = 10 ** 9 + 7

R = N - K

m = N

fac = [1] * (m + 1)
facinv = [1] * (m + 1)
for i in range(1, m+1):
    fac[i] = (fac[i-1] * i) % mod
    facinv[i] = (facinv[i-1] * pow(i, -1, mod)) % mod

def nCk(n, k):
    return (fac[n] * facinv[k] * facinv[n-k]) % mod


ans = [0] * K
for i in range(1, K+1):
    if R + 1 < i:
        break
    t = nCk(R+1, i)
    b = K - i
    t = (t * nCk(b + i - 1, b)) % mod
    ans[i-1] = t

for i in range(K):
    print(ans[i])