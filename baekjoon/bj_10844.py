N = int(input())

DP = [[0] * 10 for _ in range(N)]

DP[0] = [0,1,1,1,1,1,1,1,1,1]

for n in range(1,N):
    DP[n][0] = DP[n-1][1]
    DP[n][9] = DP[n-1][8]

    for k in range(1,9):
        DP[n][k] = DP[n-1][k-1] + DP[n-1][k+1]

print(sum(DP[N-1])%1000000000)