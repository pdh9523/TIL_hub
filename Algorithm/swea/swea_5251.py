from heapq import *

for idx in range(int(input())):

    N,E = map(int,input().split())
    graph = [[] for _ in range(N+1)]

    # 단방향 그래프 제작
    for _ in range(E):
        a,b,cost = map(int,input().split())
        graph[a].append((b,cost))

    # 다익스트라
    hq = [(0,0)]

    distance = [float('inf')] * (N+1)
    distance[0] = 0

    while hq :
        dist_now, now = heappop(hq)

        if distance[now] >= dist_now:

            for next,dist_next in graph[now] :
                cost = dist_now + dist_next

                if distance[next] > cost :
                    distance[next] = cost
                    heappush(hq,(cost,next))

    print(f"#{idx+1} {distance[N]}")