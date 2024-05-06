N = int(input())
txt = input()
ans, cnt = 0,0
for char in txt :
    if char == "(" :
        cnt += 1
    else :
        cnt -= 1
    ans = max(ans,abs(cnt))

print(-1 if cnt else ans)