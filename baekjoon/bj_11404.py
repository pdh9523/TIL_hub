import sys
from heapq import *

input = sys.stdin.readline

N,M = int(input()),int(input())

graph = [{} for _ in range(N+1)]

for _ in range(M):
    a,b,l = map(int,input().split())
    if b in graph[a]:
        graph[a][b] = min(l,graph[a][b])
    else :
        graph[a][b] = l
ans =[]
for i in range(1,N+1):
    
    q = [(0,i)]
    distance = [(float('inf'))] * (N+1)
    distance[i] = 0

    while q:
        dist_now, now = heappop(q)

        if distance[now] >= dist_now:

            for next in graph[now]:  # key : next, graph[now][key] dist_next 
                cost = dist_now + graph[now][next]
                if distance[next] > cost:
                    distance[next] = cost
                    heappush(q,(cost,next))
    for i in range(N+1):
        if distance[i] == float('inf'):
            distance[i] = 0
    print(*distance[1:])