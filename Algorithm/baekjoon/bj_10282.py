import sys
from heapq import heappush, heappop

input = sys.stdin.readline

for _ in range(int(input())):

    N,M,start = map(int,input().split())
    graph = [ [] for _ in range(N+1)]
    for _ in range(M):
        a,b,cost = map(int,input().split())
        graph[b].append((a,cost))

    hq = [(0,start)]
    distance = [float('inf')] * (N+1)
    distance[start] = 0 

    while hq : 
        dist_now, now = heappop(hq)

        if distance[now] < dist_now:
            continue
        for next, dist_next in graph[now] :
            cost = dist_now + dist_next
            if distance[next] > cost :
                distance[next] = cost
                heappush(hq, (cost,next))

    ans = 0
    max_value = 0 
    for i in distance :
        if i != float('inf') :
            ans += 1
            max_value = max(i,max_value)
    print(ans, max_value)