import sys; input = sys.stdin.readline


def bellman_ford():
    distance = [0]*(N+1)

    for i in range(N):
        for now in range(1,N+1):
            for nxt, cost in graph[now]:
                if distance[nxt] > distance[now] + cost:
                    distance[nxt] = distance[now] + cost
                    if i == N-1:
                        return True
    return False

for _ in range(int(input())):
    N,M,W = map(int,input().split())

    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        s,e,t = map(int,input().split())
        graph[s].append((e,t))
        graph[e].append((s,t))
    for _ in range(W):
        s,e,t = map(int,input().split())
        graph[s].append((e,-t))
    
    print("YES" if bellman_ford() else "NO")
