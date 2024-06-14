import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(now,depth=-1):
    if visit[now] != -1: return
    visit[now] = depth+1
    for next in sorted(graph[now]):
        dfs(next,depth+1)

N,M,R = map(int,input().split())
graph = [ [] for _ in range(N+1) ]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [-1] * (N+1)
dfs(R)
print(*visit[1:], sep="\n")