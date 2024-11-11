import sys;input = sys.stdin.readline


mod = 1000000000

N = int(input())
DP = [[dict() for _ in range(10)] for _ in range(N)]

for j in range(1,10):
    DP[0][j][1 << j] = 1

for i in range(N-1):
    for j in range(10):
        for k in DP[i][j]:
            
            v = DP[i][j][k]

            if j > 0:
                next = k | (1 << (j-1))
                if next in DP[i+1][j-1]:
                    DP[i+1][j-1][next] += v
                    DP[i+1][j-1][next] %= mod
                else:
                    DP[i+1][j-1][next] = v
                
            if j < 9:
                next = k | (1 << (j+1))
                if next in DP[i+1][j+1]:
                    DP[i+1][j+1][next] += v
                    DP[i+1][j+1][next] %= mod
                else:
                    DP[i+1][j+1][next] = v
                


mask = (1 << 10) - 1
result = 0
for d in DP[-1]:
    result += d.get(mask, 0)
        
print(result % mod)