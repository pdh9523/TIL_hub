N,M = map(int,input().split())

d = 10**9+7
DP = [ [0] * M for _ in range(N) ] 

for i in range(N) : DP[i][0] = 1
for j in range(M) : DP[0][j] = 1

for i in range(1,N):
    for j in range(1,M):
        DP[i][j] = (DP[i-1][j] + DP[i][j-1] + DP[i-1][j-1])%d
print(DP[-1][-1]%d)