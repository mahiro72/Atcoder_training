x,y = map(int,input().split())

# ans = abs(abs(x)-abs(y))
# if x<=y:
#     if 0<=x<=y or x<=y<=0:
#         print(ans)
#     else:
#         print(ans+1)
# else:
#     if 0<y<=x or y<=x<0:
#         print(ans+2)
#     else:
#         print(ans+1)
ans = [y-x,y+x+1,-y-x+1,-y+x+2]
print(min([x for x in ans if x>=0]))