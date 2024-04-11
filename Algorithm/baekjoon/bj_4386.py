import sys
from math import sqrt
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())
stars = [list(map(float,input().split())) for _ in range(N)]

graph = [[] for _ in range(N)]

# 별은 양방향으로 이을 수 있다.
for i in range(N-1):
    for j in range(i+1,N):
        cost = sqrt(abs(stars[i][0]-stars[j][0])**2 + abs(stars[i][1]-stars[j][1])**2)
        graph[i].append((j,cost))
        graph[j].append((i,cost))

hq = [(0,0)] 
visit = [False] * (N)
ans = 0

# prim
while hq : 
    dist_now, now = heappop(hq)

    if not visit[now] :
        visit[now] = True
        ans += dist_now

        for next,cost in graph[now]:
            heappush(hq,(cost,next))

# 소수점 둘째자리까지 출력
print(f"{ans:.2f}")
