N = int(input())
arr = [0]+[*map(int,input().split())]

DP = [0] * (N+1)
for i in range(1,N+1):
    for j in range(i):
        if arr[i] > arr[j]:
            DP[i] = max(DP[i], DP[j]+1)

target = max(DP)
tmp = float('inf')
ans = []
for i in range(N, 0, -1):
    if target == DP[i] and tmp > arr[i]:
        ans.append(arr[i])
        target -= 1
        tmp = arr[i]

print(len(ans))
print(*ans[::-1])
