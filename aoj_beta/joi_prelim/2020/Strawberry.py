from sys import stdin
n = int(input())
a = []

for l in stdin:
    a.append([int(val) for val in l.split()])
a.sort(reverse = True)

t = max(a[0][0], a[0][1])
x = a[0][0]
for i in range(1, n):
    t += max(x - a[i][0], a[i][1] - t)
    x = a[i][0]
t += x
print(t)

