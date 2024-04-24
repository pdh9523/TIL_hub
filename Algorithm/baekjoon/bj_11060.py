N = int(input())
arr = [*map(int,input().split())]

DP = [float('inf')] * (N+101)
DP[0] = 0

for i in range(N) :
    for j in range(1,arr[i]+1):
        DP[i+j] = min(DP[i+j],DP[i]+1)
print(DP[N-1] if DP[N-1] != float('inf') else -1)