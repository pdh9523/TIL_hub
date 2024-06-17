N = int(input())
arr = [*map(int,input().split())]

ans = 0
l,r = 0,0
cnt = [0]*10

while r<N:
    cnt[arr[r]] += 1
    r += 1
    while sum(1 for x in cnt if x) >2:
        cnt[arr[l]] -= 1
        l += 1
    ans = max(ans, r-l)
print(ans)