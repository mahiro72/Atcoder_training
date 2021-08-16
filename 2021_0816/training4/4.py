


import bisect
N = int(input())
A,B,C = (sorted(list(map(int,input().split())))for _ in range(3))

def f(x,array,is_a):
    l = 0
    r = N-1
    while l<=r:
        mid = (l+r)//2
        if array[mid]==x:
            if is_a:
                while array[mid-1]==x:
                    mid-=1
            else:
                while array[mid+1]==x:
                    mid+=1
            # print("$$",mid)
            return mid
        if array[mid]<x:
            l = mid+1
        else:
            r = mid-1
    # print("##",l,r)
    if is_a:
        return l
    return r
    
lc = len(C)
ans = 0
# print(A)
# print(B)
# print(C)
for b in B:
    # print()
    p = bisect.bisect_left(A,b)
    q = N-bisect.bisect_right(C,b)
    # p2 = f(b,A,True)
    # q2 = (N-f(b,C,False)-1)
    ans += p*q
    # print(p,q,"an")
    # print(p2,q2)
print(ans)




