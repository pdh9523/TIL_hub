import sys
from collections import deque 

input = sys.stdin.readline

N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M) :
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visit = [0] * (N+1)

cnt = 0
for i in range(1,N+1):

    if not visit[i] :
        q = deque([i])
        visit[i] = 1

        while q:
            s = q.popleft()

            for item in graph[s]:
                if not visit[item] :
                    visit[item] = 1
                    q.append(item)
        cnt += 1
print(cnt)