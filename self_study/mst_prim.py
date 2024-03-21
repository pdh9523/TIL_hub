'''
프림 MST 알고리즘 개요

하나의 정점에서 연결된 간선들 중에 하나씩 선택하면서 MST를 만들어 가는 방식
1) 임의 정점을 하나 선택해서 시작
2) 선택한 정점과 인접하는 정점들 중 최소 비용의 간선이 존재하는 정점을 선택
3) 모든 정점이 선택될 때 까지 1),2) 과정을 반복

서로소인 2개의 집합 정보를 유지
- 트리 정점 : MST를 만들기 위해 선택된 정점들
- 비트리 정점 : 선택되지 않은 정점들
'''

import heapq

N,M = map(int,input().split())  # N : 정점, M : 간선

graph = [[] for _ in range(N)] 

for _ in range(M):
    a,b,l = map(int,input().split()) # a : 출발 b : 도착 l : 비용
    graph[a].append((b,l))
    graph[b].append((a,l))

start = 0
hq = [(0,start)]
visit = [False for _ in range(N)]

ans = 0
while hq :
    dist_now, now = heapq.heappop(hq)

    if not visit[now] :
        visit[now] = True
        ans += dist_now

        for next,cost in graph[now]:
            heapq.heappush(hq,(cost,next))
            
print(ans)