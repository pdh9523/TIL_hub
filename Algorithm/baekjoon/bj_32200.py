N,X,Y = map(int,input().split())
arr = [*map(int,input().split())]

ans = 0
rest = 0

for num in arr:
    cnt = num//X
    max_v = num - Y*cnt
    if max_v > 0:
        rest += max_v
    ans += cnt

print(ans)
print(rest)