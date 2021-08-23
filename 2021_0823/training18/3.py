# s = input()
# l = len(s)
# for i in range(l):
#     for j in range(i,l):
#         if 'keyence' == (s[:i] + s[j:]):
#             print('YES')
#             exit()
# print('NO')


S = input()

for i in range(7):
    if S[:i]+S[-(7-i):] == "keyence":
        exit(print("YES"))
print("NO")