import sys
from heapq import heappop, heappush

input = sys.stdin.readline

def dijkstra(start,end) :
    
    distance = [float('inf')]*(N+1)
    distance[start] = 0

    hq = [(0,start)]

    while hq:
        dist_now, now = heappop(hq)

        if dist_now > distance[now]:continue
        
        for next, dist_next in graph[now]:
            cost = dist_next+dist_now
            if distance[next] > cost:
                distance[next]=cost
                heappush(hq,(cost,next))
    return distance[end]
    

N,M,P = map(int,input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b,cost = map(int,input().split())
    graph[a].append((b,cost))
    graph[b].append((a,cost))

if dijkstra(1,N)==dijkstra(1,P)+dijkstra(P,N):
    print("SAVE HIM")    
else :
    print("GOOD BYE")
