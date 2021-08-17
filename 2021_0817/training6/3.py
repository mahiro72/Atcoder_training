# https://atcoder.jp/contests/abc084/tasks/abc084_d

Q = int(input())
lr = [list(map(int,input().split()))for _ in range(Q)]

is_prime = [0]*(10**5+1)

def f(x):
    for i in range(1,int((x+1//2)**0.5)+1):
        if x%i==0 and i!=1:
            return 0
    return 1

def prime_check(x):
    global is_prime
    if is_prime[x]==0:
        if f(x):
            is_prime[x]==1
        else:
            is_prime[x]==-1
            return 0
    elif is_prime[x]==-1:
        return 0
    else:
        pass

    if is_prime[(x+1)//2]==0:
        if f((x+1)//2):
            is_prime[(x+1)//2]==1
            return 1
        else:
            is_prime[(x+1)//2]==-1
            return 0
    elif is_prime[(x+1)//2]==-1:
        return 0
    else:
        return 1


def f2(X):
    for x in [X,(X+1)//2]:
        for i in range(1,int((x+1//2)**0.5)+1):
            if x%i==0 and i!=1:
                return 0
    return 1

cum_prime = [0]*(10**5+1)

cnt = 0
for i in range(2,10**5+1):
    if i%2==1:
        # cnt += prime_check(i)
        cnt+=f2(i)
        cum_prime[i]=cnt
    cum_prime[i]=cnt


for l,r in lr:
    print(cum_prime[r+1]-cum_prime[l-1])

