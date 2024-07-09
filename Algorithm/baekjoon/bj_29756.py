N,M = map(int,input().split())

point = [*map(int,input().split())]
req = [*map(int,input().split())]

DP = [[-1] * 101 for _ in range(N+1)]
DP[0][100] = 0

for i in range(N):
    for j in range(101):
        if DP[i][j] == -1: continue
        HP = j - req[i]
        
        if HP >= 0:
            HP = min(100, HP + M)
            DP[i+1][HP] = max(DP[i][j] + point[i], DP[i+1][HP])
        
        HP = min(100, j + M)
        
        DP[i+1][HP] = max(DP[i+1][HP], DP[i][j])

print(max(DP[N]))
