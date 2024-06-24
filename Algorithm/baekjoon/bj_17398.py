import sys
from heapq import heappush, heappop


input = sys.stdin.readline

N,M = map(int,input().split())

# 마지막 넥서스를 제외하고, 상대 비전이 있는 곳은 방문할 수 없음
vision = [*map(int,input().split())]
vision[-1] = 0

graph = [[] for _ in range(N)]
for _ in range(M):
    a,b,cost = map(int,input().split())
    # 방문할 수 없는 경우 continue
    if vision[a] or vision[b] : continue
    # 그 외에는 graph에 양방향으로 append
    graph[a].append((b,cost))
    graph[b].append((a,cost))

# 다익스트라 
hq = [(0,0)]
distance = [float('inf')]*N
distance[0] = 0
while hq:
    dist_now, now = heappop(hq)

    if dist_now > distance[now] : continue

    for next, cost in graph[now]:
        dist_next = dist_now + cost
        if distance[next] > dist_next:
            distance[next] = dist_next
            heappush(hq,(dist_next, next))
# 초기화된 값 그대로면 -1 출력, 아니면 마지막 계산된 값 출력
print(distance[-1] if distance[-1]!=float('inf') else -1)
