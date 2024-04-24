N = int(input())
arr = [ *map(int,input().split()) ]

DP = [1] * N
# 바이토닉은 
for i in range(N-1):
    for j in range(i+1,N):
        if arr[j] > arr[i] :
            DP[j] = max(DP[j], DP[i]+1)


# 걍 최대 최소 더하면 되는거 아님?
for i in range(N-1):
    for j in range(i+1,N):
        if arr[j] < arr[i] :
            DP[j] = max(DP[j], DP[i]+1)


print(max(DP))