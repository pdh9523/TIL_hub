import sys
from heapq import heappop, heappush

input = sys.stdin.readline

V,E = int(input()), int(input())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    a,b,cost = map(int,input().split())
    graph[a].append((b,cost))
    graph[b].append((a,cost))

start = 1
visit = [False] *(V+1)
hq = [(0,start)]
ans = 0

while hq :
    dist_now, now = heappop(hq)

    if not visit[now]:
        visit[now] = True  
        ans += dist_now

        for next, cost in graph[now]:
            heappush(hq,(cost,next))
            
print(ans)