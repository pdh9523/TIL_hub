# 제일 긴 변의 길이가 나머지 두 변의 길이 합보다 작아야한다.

a = list(map(int,input().split()))
a.sort()
while sum(a)-max(a) <= max(a) :
    a[2]-=1
print(sum(a))