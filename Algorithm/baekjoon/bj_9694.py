import sys
from heapq import heappush, heappop


input = sys.stdin.readline

for tc in range(int(input())):

    N,M = map(int,input().split())

    graph = [ [] for _ in range(M) ]
    for _ in range(N) :
        a,b,cost = map(int,input().split())
        graph[a].append((b,cost))
        graph[b].append((a,cost))

    hq = [(0,0)]

    distance = [[float('inf'),[0]] for _ in range(M)]
    distance[0][0] = 0
    while hq :
        dist_now, now =  heappop(hq)

        if distance[now][0] >= dist_now :

            for next,dist_next in graph[now] :
                cost = dist_now + dist_next

                if distance[next][0] > cost :
                    distance[next][0] = cost
                    distance[next][1] = distance[now][1]+[next]
                    heappush(hq,(cost,next))

    if distance[-1][0] != float('inf'):
        print(f"Case #{tc+1}:", *distance[-1][1])
    else :
        print(f"Case #{tc+1}:", -1)