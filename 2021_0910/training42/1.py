h, w = map(int, input().split())
s = [input() for i in range(h)]
x = [[0,0,0] for i in range(h+w-1)]
for i in range(h):
  for j in range(w):
    if s[i][j] == "R":
      x[i+j][0] += 1
    elif s[i][j] == "B":
      x[i+j][1] += 1
    else:
      x[i+j][2] += 1
for i in range(h+w-1):
  if x[i][0] >= 1 and x[i][1] >= 1:
    print(0)
    exit()
ans = 1
mod = 998244353
for i in range(h+w-1):
  if x[i][0] == 0 and x[i][1] == 0:
    ans *= 2
    ans %= mod
print(ans%mod)
