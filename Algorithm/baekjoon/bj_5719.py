from sys import stdin
from heapq import heappop, heappush

input = stdin.readline

def djikstra(S,E,graph):
    hq = [(0,S)]
    distance[S] = 0

    while hq:
        dist_now, now = heappop(hq)
        if now == E: return dist_now

        for next, cost in graph[now]:
            dist_next = dist_now + cost
        
            if distance[next] > dist_next:
                distance[next] = dist_next
                heappush(hq, (dist_next,next))
                
# dfs 를 통해 최단거리 역추적이 가능
def delete(end):
    stack = [end]
    while stack :
        now = stack.pop()
        for i in range(len(reversed_graph[now])-1, -1, -1):
            prev, cost = reversed_graph[now][i]
            if distance[prev] == distance[now] - cost:
                stack.append(prev)
                del reversed_graph[now][i]

while True:
    N,M = map(int,input().split())
    if N==M==0: break
    
    S,E = map(int,input().split())

    graph = [[] for _ in range(N)]
    reversed_graph = [[] for _ in range(N)]

    for _ in range(M):
        a,b,cost = map(int,input().split())
        graph[a].append((b,cost))
        reversed_graph[b].append((a,cost))
    
    distance = [float('inf')] * N
    djikstra(S,E,graph)
    
    delete(E)

    distance = [float('inf')] * N
    djikstra(E,S,reversed_graph)

    print(distance[S] if distance[S] != float('inf') else -1)