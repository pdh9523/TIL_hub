import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())

graph =[[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[b].append(a)

ans = []
max_value = 0

for i in range(1,N+1):
    visit = [False] * (N+1)

    q = deque([(i)])
    visit[i] = True
    cnt = 0 
    while q :
        now = q.popleft()

        for next in graph[now]:
            if not visit[next] :
                visit[next] = True
                q.append(next)
                cnt += 1
    

    if cnt > max_value :
        ans = [i]
        max_value = cnt

    elif cnt == max_value :
        ans.append(i)

print(*ans)