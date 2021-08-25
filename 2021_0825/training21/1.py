# S = [x for x in input()]
# alpha = "abcdefghijklmnopqrstuvwxyz"
# S = sorted(list(set(S)))

# for s,a in zip(S,alpha):
#     print(a,s)
#     if a!=s:
#         exit(print(a))

# print("None")

S = set(x for x in input())
alpha = "abcdefghijklmnopqrstuvwxyz"

for a in alpha:
    if a not in S:
        exit(print(a))
print("None")
