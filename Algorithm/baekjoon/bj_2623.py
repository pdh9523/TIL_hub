import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int,input().split())

graph = [ [] for _ in range(N+1) ]
degree = [0] * (N+1)
for _ in range(M):
    num, *tmp = map(int,input().split())
    for i in range(num-1):
        graph[tmp[i]].append(tmp[i+1])
        degree[tmp[i+1]] += 1

q = deque()

for i in range(1,N+1):
    if degree[i] == 0 :
        q.append(i)

ans = []
while q:
    now = q.popleft()
    ans.append(now)

    for next in graph[now] :
        degree[next] -= 1

        if degree[next] == 0 :
            q.append(next)

if sum(degree) >0 :
    print(0)
else :
    for i in ans :
        print(i)