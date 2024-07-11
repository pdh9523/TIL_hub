N,M = map(int,input().split())

tree = [[] for _ in range(N+1)]

for _ in range(N-1):
    a,b,cost = map(int,input().split())
    tree[a].append((b,cost))
    tree[b].append((a,cost))

for _ in range(M):
    s,e = map(int,input().split())
    visit = [0]*(N+1)
    stack = [(s,0)]

    while stack:
        now,dist = stack.pop()

        if now == e: exit(print(dist))
        if visit[now]: continue

        visit[now] = 1
        for next,cost in tree[now]:
            stack.append((next,dist+cost))