N = int(input())

arr = [0] + list(map(int,input().split()))

DP = [0] * (N+1)

for i in range(N+1):
    for j in range(i):
        if arr[i] > arr[j]:
            DP[i] = max(DP[i],DP[j]+1)

print(max(DP))