N,M,V = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)


stack = [V]
visit = [0] * (N+1)
DFS = [V]
visit[V] = 1
while stack:
    tc = stack.pop()
    if visit[tc] == 0 :
        DFS.append(tc)
        visit[tc] = 1
    for item in sorted(graph[tc], reverse= True):
        if visit[item] == 0 :
            stack.append(item)

q = [V]
visit = [0] * (N+1)
BFS = []
visit[V] =1
while q :
    tc = q.pop(0)
    BFS.append(tc)

    if len(BFS) == N:
        break
    for item in sorted(graph[tc]):
        if visit[item] == 0 :
            q.append(item)
            visit[item] = 1
            

print(*DFS)
print(*BFS)