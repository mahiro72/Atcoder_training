# https://atcoder.jp/contests/abc057/tasks/abc057_c

N = int(input())
def f(x):
    s = set()
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            s.add(i)
    return list(s)

ans = 10**10
for a in f(N):
    b = N//a
    f_min = max(len(str(a)),len(str(b)))
    ans = min(ans,f_min)
print(ans)
