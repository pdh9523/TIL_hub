import sys; input = sys.stdin.readline


def bellman_ford():
    distance = [0]*(N+1)

    arr = [*range(1,N+1)]
    visit = set()
    while arr:
        tmp = tuple(arr)
        if tmp in visit:
            return True
        
        visit.add(tmp)
        tmp = []

        for now in arr:
            for nxt, cost in graph[now]:
                if distance[nxt] > distance[now] + cost:
                    distance[nxt] = distance[now] + cost
                    tmp.append(nxt)
        
        arr = tmp
    print(distance)
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