import heapq

N,M = map(int,input().split())
A = list(map(lambda x:-int(x),input().split()))
hq = A
heapq.heapify(hq)

while M>0:
    a = heapq.heappop(hq)
    heapq.heappush(hq,-((-a)//2))
    M-=1

print(-sum(A))