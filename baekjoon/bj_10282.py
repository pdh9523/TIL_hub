import sys
from heapq import *

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N,D,C = map(int,input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(D):
        a,b,l = map(int,input().split())
        graph[b].append((a,l))

    q = [(0,C)]
    distance = [float('inf')] * (N+1)
    distance[C] = 0

    route = [0] * (N+1)

    while q :
        dist_now, now = heappop(q)

        if distance[now] >= dist_now :

            for next, dist_next in graph[now]:
                cost = dist_now + dist_next
                if distance[next] > cost:
                    distance[next] = cost
                    route[now] = 1
                    heappush(q,(cost, next))
    
    print(sum(route)+1, max(filter(lambda x: x != float("inf"), distance)))