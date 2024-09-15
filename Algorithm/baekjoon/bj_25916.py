N,M = map(int,input().split())
arr = [*map(int,input().split())]

left,right = 0,0
ans, now = 0, arr[0]

while True:
    if now==M:
        ans = M
        break
    
    if M>now:
        ans = max(ans, now)
        right += 1
        if right>=N: break
        now += arr[right]
    else:
        now -= arr[left]
        left += 1

print(ans)