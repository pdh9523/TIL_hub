N,M = map(int,input().split())
arr = sorted([int(input()) for _ in range(M)], reverse=True)

max_v = 0
ans = 0

for i in range(M):
    if (i+1) > N: break
    if arr[i] * (i+1) > max_v:
        ans = arr[i]
        max_v = arr[i] * (i+1)

print(ans, max_v)