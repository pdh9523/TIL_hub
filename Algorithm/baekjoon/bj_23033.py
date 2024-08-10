import sys
from math import ceil
from heapq import heappop, heappush

input = sys.stdin.readline

def dijkstra():
    while hq:
        time_now, now = heappop(hq)
        if time_now > distance[now] : continue
        for nxt, cost, schedule in graph[now]:
            time_nxt = cost + ceil(time_now/schedule)*schedule  # 현재 시간 (time_now 가 schedule의 배수와 맞춰져야함) 
            if distance[nxt] > time_nxt:
                distance[nxt] = time_nxt
                heappush(hq, (time_nxt, nxt))

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    A,B,T,W = map(int,input().split())
    graph[A].append((B,T,W))

distance = [float("inf")] * (N+1)
distance[1] = 0

hq = [(0,1)]
dijkstra()
print(distance[N])