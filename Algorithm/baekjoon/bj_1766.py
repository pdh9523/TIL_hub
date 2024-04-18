import sys
from heapq import heappop, heappush

input = sys.stdin.readline


N,M = map(int,input().split())

graph = [ [] for _ in range(N+1)]
degree = [0] * (N+1)

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    degree[b] += 1

hq = []

for i in range(1,N+1):
    if degree[i] == 0 :
        heappush(hq,i)

ans = []
while hq :
    now = heappop(hq)
    ans.append(now)
    for next in graph[now] :
        degree[next] -= 1
        if degree[next] == 0 :
            heappush(hq,next)

print(*ans)