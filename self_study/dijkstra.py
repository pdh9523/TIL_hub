import heapq

n,r = map(int,input().split())                  # n : 정점의 개수 r : 노드의 개수

graph = [[] for _ in range(n+1)]                # 인접 그래프

for _ in range(r):
    a,b,l = map(int,input().split())            # a : 출발 b : 도착 l : 거리
    graph[a].append((b,l))
    graph[b].append((a,l))

distance = [float('inf')] * (n+1)               # distance : 거리

start = 1                                       # start : 초기값
distance[start] = 0                             # 시작점은 거리가 0 
q = [(0,start)]                                 # q에 (0, 시작점) 을 담고 출발
while q:
    dist_now, now = heapq.heappop(q)            # 최소값부터 계산 (dist : 현재 누적된 거리, now : 현재위치)

    if distance[now] >= dist_now:               # 현재 누적된 거리가 거리 리스트에 기록된 거리보다 짧을 경우
        for next, dist_next in graph[now]:      # 인접 그래프에서 next와 next의 거리를 추출해서
            cost = dist_now + dist_next         # cost : 현재 거리 + 다음 거리
            if cost < distance[next]:           # 지금 위치에서 가는 방법이 더 짧은 경우
                distance[next] = cost           # 값 변경
                heapq.heappush(q,(cost,next))   # (cost,next) q에 푸시

print(distance)                         # 각 정점으로 향하는 최소 거리