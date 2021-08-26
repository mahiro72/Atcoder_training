mt = [int(input())for _ in range(10)]
mt.sort(reverse=True)
print(*mt[:3],sep="\n")