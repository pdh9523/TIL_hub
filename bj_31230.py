import sys; input = sys.stdin.readline
from heapq import heappush, heappop


def dijkstra(n):
    hq = [(0,n)]
    distance = [float('inf')] * (N+1)
    distance[n] = 0

    while hq:
        dist_now, now = heappop(hq)
        if dist_now > distance[now]: continue

        for nxt, cost in graph[now]:
            dist_nxt = dist_now + cost
            if distance[nxt] > dist_nxt:
                distance[nxt] = dist_nxt
                heappush(hq, (dist_nxt, nxt))
    return res.append(distance)

N,M,A,B = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,d = map(int,input().split())
    graph[a].append((b,d))
    graph[b].append((a,d))

res = []
for i in A,B:
    dijkstra(i)
res = [*map(sum, zip(*res))]

min_v = min(res)
if min_v == float('inf') : exit(print(0))

ans = []
for i in range(1,N+1):
    if res[i] == min_v:
        ans.append(i)
print(len(ans))
print(*ans)