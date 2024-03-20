import sys
from heapq import *

input = sys.stdin.readline

N,M = int(input()), int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b,l = map(int,input().split())
    graph[a].append((b,l))

start, end = map(int,input().split())

q = [(0,start)]
distance = [float('inf')] * (N+1)
distance[start] = 0
while q :
    dist_now, now = heappop(q)

    if distance[now] >= dist_now:
        for next, dist_next in graph[now] :
            cost = dist_now + dist_next
            if distance[next] > cost :
                distance[next] = cost
                heappush(q,(cost, next))

print(distance[end])