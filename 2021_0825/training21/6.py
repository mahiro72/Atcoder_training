from collections import Counter
S = input()
T = input()

ss = sorted(list(Counter(S).values()))
tt = sorted(list(Counter(T).values()))

print("Yes" if ss==tt else "No")