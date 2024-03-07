N,M,V = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

stack = [V]                                         # DFS - stack
visit = [0] * (N+1)                                 # visit : 방문 여부
DFS = [V]                                           # DFS : 방문 경로
visit[V] = 1                                        # 첫 시작점 방문 체크
while stack:                                        # DFS 시작
    tc = stack.pop()
    if visit[tc] == 0 :
        DFS.append(tc)
        visit[tc] = 1
    for item in sorted(graph[tc], reverse= True):   # 스택은 후입선출이므로 오름차순으로 순회하려면 내림차순으로 쌓아야한다
        if visit[item] == 0 :
            stack.append(item)


q = [V]                                             # BFS - queue
visit = [0] * (N+1)                                 # visit : 방문 여부(2)
BFS = []                                            # BFS : 방문 경로
visit[V] =1                                         # 첫 시작점 방문 체크
while q :                                           # BFS 시작
    tc = q.pop(0)
    BFS.append(tc)

    if len(BFS) == N:
        break
    for item in sorted(graph[tc]):                  # 큐는 선입선출이므로 오름차순으로 정렬해서 순회하면 됨
        if visit[item] == 0 :
            q.append(item)
            visit[item] = 1
            
print(*DFS)     # 출력
print(*BFS)