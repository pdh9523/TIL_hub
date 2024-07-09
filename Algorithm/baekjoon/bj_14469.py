arr = sorted([[*map(int,input().split())] for _ in range(int(input()))])

ans = 0 
for s,e in arr:
    if ans < s:
        ans = s
    ans += e

print(ans)