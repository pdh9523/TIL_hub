from math import sqrt
ans = float('inf')
yumi = list(map(int,input().split()))

man1 = list(map(int,input().split()))
# a
man2 = list(map(int,input().split()))
# b
man3 = list(map(int,input().split()))
# c
# man 1

A = sqrt((yumi[0] - man1[0])**2 + (yumi[1] - man1[1])**2)
B = sqrt((yumi[0] - man2[0])**2 + (yumi[1] - man2[1])**2)
C = sqrt((yumi[0] - man3[0])**2 + (yumi[1] - man3[1])**2)


a = sqrt((man1[0] - man2[0])**2 + (man1[1] - man2[1])**2)
b = sqrt((man2[0] - man3[0])**2 + (man2[1] - man3[1])**2)
c = sqrt((man3[0] - man1[0])**2 + (man3[1] - man1[1])**2)
#123
tmp = int(A+a+b)
ans = min(tmp,ans)
#132
tmp = int(A+b+c)
ans = min(tmp,ans)
#213
tmp = int(B+a+c)
ans = min(tmp,ans)
#231
tmp = int(B+b+c)
ans = min(tmp,ans)
#321
tmp = int(C+b+a)
ans = min(tmp,ans)
#312
tmp = int(C+c+a)
ans = min(tmp,ans)

print(ans)