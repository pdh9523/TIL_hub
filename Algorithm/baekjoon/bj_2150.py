import sys; input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(now):
    visit[now] = 1
    for nxt in graph[now]:
        if not visit[nxt]:
            dfs(nxt)
    stack.append(now)


def sfd(now):
    visit[now] = 1
    scc.append(now)
    for nxt in rev_graph[now]:
        if not visit[nxt]:
            sfd(nxt)


N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
rev_graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    rev_graph[b].append(a)

stack = []
visit = [0]*(N+1)
for i in range(1, N+1):
    if not visit[i]:
        dfs(i)

visit = [0]*(N+1)
ans = []
while stack:
    scc = []
    now = stack.pop()
    if not visit[now]:
        sfd(now)
        ans.append(sorted(scc))

print(len(ans))
for i in sorted(ans):
    print(*i, -1)
