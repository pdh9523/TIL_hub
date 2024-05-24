import sys
from heapq import heappop, heappush


input = sys.stdin.readline

def dijsktra(start,end):
    hq = [(0,start)]
    distance = [float('inf')] * (V+1)
    distance[start] = 0

    while hq :
        dist_now, now = heappop(hq)

        if dist_now > distance[now] : continue

        for next, cost in graph[now]:
            dist_next = dist_now + cost
            if distance[next] > dist_next :
                distance[next] = dist_next
                heappush(hq,(dist_next,next))
    return -1 if distance[end]==float('inf') else distance[end]

N,V,E = map(int,input().split())
KIST,CIAL = map(int,input().split())
staff = [*map(int,input().split())]

graph = [ [] for _ in range(V+1) ]
for _ in range(E) :
    a,b,cost = map(int,input().split())
    graph[a].append((b,cost))
    graph[b].append((a,cost))
ans = 0 
for i in staff:
   ans += dijsktra(i,KIST) + dijsktra(i,CIAL)
print(ans)