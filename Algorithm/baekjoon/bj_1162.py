import sys; input = sys.stdin.readline
from heapq import heappop, heappush


N,M,K = map(int,input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,d = map(int,input().split())

    graph[a].append((b,d))
    graph[b].append((a,d))

distance = [[float('inf')]*(K+1) for _ in range(N+1)]
cnt = 0
# dist, cnt, start
hq = [(0,0,1)]
distance[1][0] = 0

while hq:
    dist_now, cnt, now = heappop(hq)
    if dist_now > distance[now][cnt]: continue

    for nxt, cost in graph[now]:
        dist_next = dist_now + cost
        if distance[nxt][cnt] > dist_next:
            distance[nxt][cnt] = dist_next
            heappush(hq, (dist_next, cnt, nxt))
        
        if cnt < K and distance[nxt][cnt+1] > dist_now:
            distance[nxt][cnt+1] = dist_now
            heappush(hq, (dist_now, cnt+1, nxt))

print(min(distance[N]))