t = int(input())
arr = [1001]+list(map(int,input().split()))

DP = [0]*(t+1)

for i in range(t+1):
    for j in range(i):
        if arr[j] > arr[i]:
            DP[i] = max(DP[i], DP[j]+1)
print(max(DP))