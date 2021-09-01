import bisect

N = int(input())
r,g,b=[],[],[]
INF = float('inf')
 
for i in range(2*N):
    a,c = map(str,input().split())
    a = int(a)
    if c=='R':r.append(a)
    elif c=='G':g.append(a)
    else:b.append(a)
 

def solve(a_list,b_list):
    ans = INF
    for a in a_list:
        i = bisect.bisect_right(b_list,a)
        if i==len(b_list):
            ans = min(ans,abs(b_list[-1]-a))
        else:
            ans = min(ans,abs(b_list[i]-a),abs(b_list[i-1]-a))
    return ans

lr,lg,lb = len(r),len(g),len(b)

if lr%2==0 and lg%2==0 and lb%2==0:
    exit(print(0))
elif lr%2==0:
    x, y, z = g, b, r
elif lg%2 == 0:
    x, y, z = r, b, g
else:
    x, y, z = r, g, b

x = sorted(x)
y = sorted(y)
z = sorted(z)

print(min(solve(x,y),solve(z,x)+solve(z,y)))






