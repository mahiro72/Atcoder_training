# https://atcoder.jp/contests/abc181/tasks/abc181_c

from itertools import combinations

N = int(input())
xy = [list(map(int,input().split()))for _ in range(N)]

for (x1,y1),(x2,y2),(x3,y3) in combinations(xy,3):
    if (y2-y1)*(x3-x1)==(x2-x1)*(y3-y1):
        exit(print("Yes"))
print("No")