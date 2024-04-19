N = int(input())

arr = list(map(int,input().split()))
DP = arr[:]
for i in range(N-1):
    for j in range(i+1,N):
        if arr[j] > arr[i] :
            DP[j] = max(DP[j], DP[i]+arr[j])

print(max(DP))