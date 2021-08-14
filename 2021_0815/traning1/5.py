import math
n, m = map(int, input().split())
print(math.floor(pow(10, n,m*m)/m)%m)