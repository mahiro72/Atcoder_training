from collections import Counter

w = input()
c = Counter(w)
for i in c.values():
    if i%2==1:
        exit(print("No"))
print("Yes")