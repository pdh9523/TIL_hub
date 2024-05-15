import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def rational_path(now):
    if DP[now] == 0:
        for next, _ in graph[now]:
            if distance[now] > distance[next]:
                DP[now] += rational_path(next)

    return DP[now]

S,T = 1,2
N,M = map(int,input().split())

graph = [ [] for _ in range(N+1) ]
for _ in range(M):
    a,b,cost = map(int,input().split())
    graph[a].append((b,cost))
    graph[b].append((a,cost))


start = T
distance = [float('inf')] * (N+1)
distance[start] = 0
hq = [(0,start)]


while hq :
    dist_now, now = heappop(hq)

    if dist_now > distance[now] : continue

    for next, dist_next in graph[now] :
        cost = dist_now + dist_next

        if distance[next] > cost :
            distance[next] = cost
            heappush(hq, (cost,next))

DP = [0] * (N+1)
DP[2] = 1
print(rational_path(S))