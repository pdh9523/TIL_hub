import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

dr = (1,0),(0,1),(-1,0),(0,-1)

def dfs(i=0,j=0):
    if i==N-1 and j==M-1: return 1
    
    if DP[i][j] == - 1 :
        DP[i][j] = 0
        for dx,dy in dr :
            di,dj = i+dx, j+dy
            if 0 <= di < N and 0 <= dj < M :
                if arr[i][j] > arr[di][dj] :
                    DP[i][j] += dfs(di,dj)
    return DP[i][j]

N,M = map(int,input().split())
arr = [ [*map(int,input().split())] for _ in range(N) ]
DP = [ [-1] * M for _ in range(N) ] 
print(dfs())