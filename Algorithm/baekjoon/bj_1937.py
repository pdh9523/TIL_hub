import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(x,y):
    if DP[x][y]: return DP[x][y]
    DP[x][y] = 1
    for dx, dy in dr:
        di, dj = x+dx, y+dy
        if 0 <= di < N and 0 <= dj < N and arr[x][y] < arr[di][dj]:
            DP[x][y] = max(DP[x][y], dfs(di,dj)+1)
    return DP[x][y]


dr = (-1,0), (0,-1), (0,1), (1,0)

N = int(input())
arr = [[*map(int,input().split())] for _ in range(N)]
DP = [[0]*N for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        ans = max(ans, dfs(i,j))
print(ans)
