import math

S = int(input())
M = 10**9
y = math.ceil(S/M)
x = y*M-S

print(0,0,M,1,x,y)