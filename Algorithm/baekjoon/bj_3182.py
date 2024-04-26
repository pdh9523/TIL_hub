N = int(input())

graph = [ [] for _ in range(N+1) ]

for i in range(1,N+1):
    graph[i].append(int(input()))

ans = 0
tmp = 0

for i in range(1,N+1):
    
    stack = [i]
    visit = [0]*(N+1)

    while stack:
        now = stack.pop()
        if not visit[now] :
            visit[now] = 1
            for next in graph[now]:
                stack.append(next)

    if sum(visit) > tmp :
        ans = i
        tmp = sum(visit)

print(ans)