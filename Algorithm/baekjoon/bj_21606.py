N = int(input())
S = input()

graph= [ [] for _ in range(N+1)]
for _ in range(N):
    a,b = map(int,input().split())
    graph[a].append(b)
