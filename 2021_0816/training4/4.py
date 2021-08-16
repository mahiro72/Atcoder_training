# https://atcoder.jp/contests/arc084/tasks/arc084_a
import bisect
N = int(input())
A,B,C = (sorted(list(map(int,input().split())))for _ in range(3))
ans = 0
for b in B:
    p = bisect.bisect_left(A,b)
    q = N-bisect.bisect_right(C,b)
    ans += p*q
print(ans)