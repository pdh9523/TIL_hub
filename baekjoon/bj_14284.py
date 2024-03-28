from heapq import heappop, heappush

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b,cost = map(int,input().split())

    graph[a].append((cost,b))
    graph[b].append((cost,a))

s,t = map(int,input().split())

hq = [(0,s)]
distance = [float('inf')] * (N+1)
distance[s] = 0

while hq :
    dist_now, now = heappop(hq)

    if distance[now] >= dist_now :

        for dist_next, next in graph[now]:
            cost = dist_now + dist_next
            if distance[next] > cost :
                distance[next] = cost 
                heappush(hq,(cost,next))

print(distance[t])