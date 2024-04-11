import sys
from heapq import heappush, heappop

input = sys.stdin.readline


N,M = map(int,input().split())
while (N,M) != (0,0):

    graph = [[] for _ in range(N)]
    ans = 0
    for _ in range(M):
        a,b,cost = map(int,input().split())
        graph[a].append((cost,b))
        graph[b].append((cost,a))
        ans += cost

    hq = [(0,0)]
    visit = [False] * N
    while hq :
        dist_now, now = heappop(hq)

        if not visit[now]:

            visit[now] = True
            ans -= dist_now
            for item in graph[now]:
                heappush(hq,item)

    print(ans)
    N,M = map(int,input().split())