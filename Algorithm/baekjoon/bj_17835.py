import sys
from heapq import heappop, heappush

input = sys.stdin.readline
N, M, K = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, cost = map(int,input().split())
    graph[b].append((a, cost))

distance = [float('inf')]*(N+1)
hq = []
for i in map(int,input().split()):
    distance[i] = 0
    heappush(hq, (0, i))

while hq:
    dist_now, now = heappop(hq)

    if dist_now > distance[now]: continue

    for nxt, cost in graph[now]:
        dist_nxt = dist_now + cost

        if distance[nxt] > dist_nxt:
            distance[nxt] = dist_nxt
            heappush(hq, (dist_nxt, nxt))

ans, ans_dist = 0, 0
for i,v in enumerate(distance[1:], start=1):
    if v > ans_dist:
        ans_dist = v
        ans = i
print(ans)
print(ans_dist)
