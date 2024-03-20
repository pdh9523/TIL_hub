import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N,M = map(int,input().split())

graph=[[] for _ in range(N+1)]

for _ in range(M):
    a,b,l = map(int,input().split())
    graph[a].append((b,l))
    graph[b].append((a,l))


q = [(0,1)]
distance = [float('inf')] * (N+1)
distance[1] = 0

while q:
    dist_now, now = heappop(q)

    if distance[now] >= dist_now:

        for next, dist_next in graph[now]:
            cost = dist_now + dist_next
            if distance[next] > cost:
                distance[next] = cost
                heappush(q, (cost,next))

print(distance[N])