N = int(int(input()))

graph = [list(map(lambda x : int(x) if x == "1" else float('inf') , input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    print()
    for i in graph: 
        print(*i)
    print()
ans = [[0 if graph[i][j]==float('inf') else 1 for j in range(N)] for i in range(N)]

for i in ans :
    print(*i)