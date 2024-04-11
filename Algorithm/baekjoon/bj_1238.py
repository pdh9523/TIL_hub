# 파티. 걍 다익스트라 왔다갔다 두번하면 되는거아님?
import sys
from heapq import *

input = sys.stdin.readline

def dijkstra():
    while q :
        dist_now ,now = heappop(q)

        if distance[now] >= dist_now:

            for next, dist_next in graph[now]:
                cost = dist_now + dist_next
                if distance[next] > cost:
                    distance[next] = cost
                    heappush(q,(cost,next))


N,M,X = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b,l = map(int,input().split())
    graph[a].append((b,l))

x = [0]

for i in range(1,N+1):
    start = i
    q = [(0,i)]
    distance = [float("inf")] * (N+1)
    distance[i] = 0
    dijkstra()
    x.append(distance[X])

q = [(0,X)]
distance = [float("inf")] * (N+1)
distance[X] = 0
dijkstra()


print(max(map(lambda x : sum(x) if not float("inf") in x else 0, zip(distance,x))))