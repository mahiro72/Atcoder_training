N,M = map(int,input().split())
S = [input() for _ in range(N)]
even_odd = [0,0]
for i in range(N):
    even_odd[S[i].count("1")%2]+=1
print(even_odd[0]*even_odd[1])