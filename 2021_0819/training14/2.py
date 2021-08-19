H,W = map(int,input().split())

root = 0
for i in range(H):
    a = input()
    root += a.count("#")

if root==(H+W-1):
    print("Possible")
else:
    print("Impossible")