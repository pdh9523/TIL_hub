import sys
from collections import deque


input = sys.stdin.readline

N = int(input())

graph = [ [] for _ in range(N+1) ]
times = [0] 
degree = [0] * (N+1)
DP = [0] * (N+1)

for i in range(1,N+1):
    time, *arr , _ = map(int,input().split())
    times.append(time)
    for j in arr :
        graph[j].append(i)
        degree[i] +=1

q = deque()

for i in range(1,N+1):
    if degree[i] == 0 :
        q.append(i)
        DP[i] = times[i]

while q :
    now = q.popleft()

    for next in graph[now] :
        degree[next] -= 1

        DP[next] = max(DP[next], DP[now]+times[next])

        if degree[next] == 0 :
            q.append(next)


for i in range(1,N+1):
    print(DP[i])