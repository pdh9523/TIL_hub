import sys
input = sys.stdin.readline
INF = int(1e9)


def convert(char):
    # a = 97, A = 65
    # 소문자가 더 크니까 먼저 처리
    if ord(char) >= ord("a"):
        return ord(char)-ord("a")+26

    return ord(char)-ord("A")


def make_flow(start, end, path):
    min_v = float("inf")

    now = end
    while now != start:
        nxt = path[now]
        min_v = min(min_v, capacity[nxt][now] - flow[nxt][now])
        now = nxt

    now = end
    while now != start:
        nxt = path[now]
        flow[nxt][now] += min_v
        flow[now][nxt] -= min_v
        now = nxt

    return min_v


def bfs(start, end):
    path = [-1]*52
    queue = [start]

    for now in queue:
        for nxt in graph[now]:
            if capacity[now][nxt] - flow[now][nxt] > 0 > path[nxt]:
                queue.append(nxt)
                path[nxt] = now

                # 경로 만들어서 넘기기
                if nxt == end:
                    return make_flow(start, end, path)
    return 0


def edmonds_karp(start, end):
    max_flow = 0
    while True:
        cost = bfs(start, end)
        if cost > 0:
            max_flow += cost
        else:
            return max_flow


N = int(input())
flow = [[0]*52 for _ in range(52)]
capacity = [[0]*52 for _ in range(52)]
graph = [[] for _ in range(52)]

for _ in range(N):
    u,v,w = input().split()
    u,v,w = convert(u), convert(v), int(w)

    capacity[u][v] += w
    capacity[v][u] += w

    graph[u].append(v)
    graph[v].append(u)

print(edmonds_karp(convert("A"), convert("Z")))
