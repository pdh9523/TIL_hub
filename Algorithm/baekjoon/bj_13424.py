import sys
from heapq import *

input = sys.stdin.readline

for _ in range(int(input())):

    N,M = map(int,input().split())
    graph=[[] for _ in range(N+1)]
    for _ in range(M):
        a,b,l = map(int,input().split())
        graph[a].append((b,l))
        graph[b].append((a,l))
    
    K = int(input())
    friend = list(map(int,input().split()))
    ans = 0
    total = float('inf')
    for i in range(1,N+1):
        q = [(0,i)]

        distance = [float('inf')] * (N+1)
        distance[i] = 0
        while q :
            dist_now, now = heappop(q)

            if distance[now] >= dist_now :

                for next, dist_next in graph[now]:

                    cost = dist_now + dist_next

                    if distance[next] > cost:
                        distance[next] = cost
                        heappush(q,(cost,next))
        tmp = 0
        for x in friend:
            tmp += distance[x]
        if total > tmp:
            total = tmp
            ans = i
    print(ans)