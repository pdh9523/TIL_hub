N, M = int(input()), int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M) :
    a,b,l = map(int,input().split())
    graph[a].append((b,l))