import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(now=1):
    visit[now] = 1

    for nxt in graph[now]:
        if not visit[nxt]:

            dfs(nxt)

            DP[now][1] += DP[nxt][0]
            DP[now][0] += max(DP[nxt][0], DP[nxt][1])


N = int(input())
cost = [0] + [*map(int,input().split())]

visit = [0]*(N+1)
DP = [[0, cost[i]]*2 for i in range(N+1)]

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs()

print(max(DP[1][1], DP[1][0]))