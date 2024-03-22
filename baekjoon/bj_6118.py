import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([1])

visit = [0] * (N+1)
visit[1] = 1
while q:
    now = q.popleft()

    for next in graph[now]:
        if not visit[next]:
            visit[next] = visit[now] + 1
            q.append(next)

dist = max(visit)
num  = visit.index(dist)
cnt  = visit.count(dist)

print(num, dist-1, cnt)