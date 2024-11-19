arr = sorted([[*map(int,input().split())] for _ in range(int(input()))])

ans = 0
start = arr[0][0]
end = arr[0][1]

for s,e in arr[1:]:
    if end < s:
        ans += end-start
        start = s
    end = max(e,end)
    
ans += end-start
print(ans)