from math import ceil

N = int(input())
arr = [*map(int,input().split())]
main,sub = map(int,input().split())

ans = 0
for num in arr:
    num -= main
    ans += 1
    if num>0:
        ans += ceil(num/sub)
print(ans)