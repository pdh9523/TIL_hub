from collections import deque 


N = int(input())

graph = [[] for _ in range(N)]

for i in range(N):
    arr = list(map(int,input().split()))
    for j in range(N) :
        if arr[j] == 1: 
            graph[i].append(j)
            graph[j].append(i)

visit = [[0]*N for _ in range(N)]

for i in range(N):
    q = deque([i])

    while q :
        
        now = q.popleft()

        for next in graph[now]:
            if not visit[now][next] : 
                visit[now][next] = 1
                visit[next][now] = 1
                q.append(next)
print(visit)