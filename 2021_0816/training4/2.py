# https://atcoder.jp/contests/abc046/tasks/abc046_b

N,K = map(int,input().split())
print(K*pow(K-1,N-1))