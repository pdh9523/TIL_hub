N,K = map(int,input().split())

doll = list(map(int,input().split()))


left = 0
right = 0
ans = float('inf')

cnt = 0 

if doll[0] == 1:
    cnt += 1


while right < N :
    if cnt < K :
        right += 1
        if right < N and doll[right] == 1 :
            cnt += 1
    else :
        ans = min(right-left+1, ans)
        if doll[left] == 1:
            cnt -= 1
        left += 1

if ans == float('inf') :
    print(-1)
else :
    print(ans)