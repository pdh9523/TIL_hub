import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]

DP = [0] * (N+1)
degree = [0] * (N+1)
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    degree[b] += 1

q = deque()
for i in range(1,N+1):
    if degree[i] == 0 :
        q.append((i,1))
        DP[i] += 1

while q :
    now, d = q.popleft()
    for next in graph[now]:
        degree[next] -= 1
        if degree[next] == 0 :
            q.append((next,d+1))
            DP[next] = d+1

print(*DP[1:])