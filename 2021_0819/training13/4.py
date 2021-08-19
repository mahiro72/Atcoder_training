N = int(input())
ab = []
for i in range(N):
    a,b = map(int,input().split())
    ab.append((a+b,a,b))

ab.sort(key=lambda x:x[0],reverse=True)

people = [0,0]
for i in range(N):
    people[i%2]+=ab[i][1 if i%2==0 else 2]
print(people[0]-people[1])
