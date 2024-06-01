import sys


input = sys.stdin.readline

N,M = map(int,input().split())

graph = [[float('inf')] * (N+1) for _ in range(N+1)]

for i in range(1,N+1):
    graph[i][i] = 0

for _ in range(M):
    a,b,cost = map(int,input().split())
    graph[a][b] = cost

for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])

ans = float('inf')
for i in range(1,N):
    for j in range(i+1,N+1):
        ans = min(ans, graph[i][j]+graph[j][i])

print(ans if ans != float('inf') else -1)
