dr = (1,0),(0,1),(-1,0),(0,-1)

N,M = map(int,input().split())
load = [ [*map(int,input().split())] for _ in range(N) ]

DP = [ [0] * M for _ in range(N) ]

DP[0][0] = 1

for i in range(N):
    for j in range(M):
        for dx,dy in dr:
            di,dj = i+dx, j+dy
            if 0 <= di < N and 0 <= dj < M:
                if load[i][j] > load[di][dj]:
                    DP[di][dj] += DP[i][j]

print(DP)