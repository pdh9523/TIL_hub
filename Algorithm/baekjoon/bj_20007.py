import sys
from heapq import heappop, heappush


input = sys.stdin.readline

N,M,X,Y = map(int,input().split())

graph = [[] for _ in range(N)]
for _ in range(M):
    a,b,cost = map(int,input().split())
    graph[a].append((b,cost))
    graph[b].append((a,cost))

distance = [float('inf')] * N
distance[Y] = 0

hq = [(0,Y)]
while hq:
    dist_now, now = heappop(hq)
    if dist_now > distance[now]: continue
    for nxt, cost in graph[now]:
        dist_nxt = dist_now + cost
        if distance[nxt] > dist_nxt:
            distance[nxt] = dist_nxt
            heappush(hq,(dist_nxt,nxt))

ans,tmp = 0,0

for dist in sorted(map(lambda x: 2*x, distance)):
    if dist > X: exit(print(-1))
    if tmp + dist > X:
        tmp = 0 
        ans += 1
    
    tmp += dist
if tmp: ans += 1
print(ans)