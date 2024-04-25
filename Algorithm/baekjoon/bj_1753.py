import sys
from heapq import heappush, heappop

input = sys.stdin.readline
N,M = map(int,input().split())
start = int(input())


graph = [ [] for _ in range(N+1) ]
for _ in range(M):
    a,b,l = map(int,input().split())
    graph[a].append((b,l))


INF = float('inf')


distance = [ INF ] * (N+1)
distance[start] = 0

hq = [(0,start)]
while hq :
    dist_now, now = heappop(hq)

    if dist_now > distance[now] : continue

    for next, dist_next in graph[now] :
        cost = dist_now + dist_next
        if distance[next] > cost :
            distance[next] = cost

            heappush(hq,(cost,next))

for i in distance[1:] :
    print(i if i != INF else "INF")