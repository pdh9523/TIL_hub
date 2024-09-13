from heapq import heappush, heappop

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
ans = 0
for _ in range(M):
    a,b,c = map(int,input().split())
    ans += c
    graph[a].append((c,b))
    graph[b].append((c,a))

visit = [0]*(N+1)
cnt = 0
hq = [(0,1)]
while hq:
    cost,now = heappop(hq)

    if not visit[now]:
        cnt += 1
        ans -= cost
        visit[now] = 1
        for node in graph[now]:
            heappush(hq, node)
print(-1 if cnt != N else ans)
