T = int(input())
S = [input()for _ in range(T)]

def solve(x):
    a = 'atcoder'
    if a<x:
        return 0
    elif set(x) == {'a'}:
        return -1
    else:
        INF = 10**5
        ans = INF
        for i in range(1,len(x)):
            if x[i]=='a':continue
            if x[i]>'t':
                ans = min(ans,i-1)
            else:
                ans = min(ans,i)
        return ans


for s in S:
    print(solve(s))

