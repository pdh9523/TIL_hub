# 뱀과 사다리 게임
import sys
from collections import deque

input = sys.stdin.readline


N,M = map(int,input().split())
# 시작점은 1, 도착점은 100으로 고정
start, end = 1,100
graph = [ [] for _ in range(end+1)]     # 도착점 +1 만큼의 리스트 초기화

# 사다리
for _ in range(N):
    a,b = map(int,input().split())
    graph[a].append(b)

# 뱀
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)

# BFS 준비
q = deque([start])
visit = [0] * (end+1)
visit[start] = 1
# BFS
while q :
    now = q.popleft()

    for dice in range(6,0,-1) :
        next = now + dice
        # 100을 넘어서는 경우 중단 (99에서 1만큼 가야하는 경우도 있으므로 break가 아닌 continue)
        if next > end :
            continue
        # 방문했다면 continue
        if visit[next] : continue
        # 그래프에 뭔가 있다면 (뱀/사다리)
        if graph[next] :
            # next를 갱신하기
            next = graph[next][0]
            # 갱신한 next를 방문했다면 continue
            if visit[next] : continue
        # 거리 계산
        visit[next] = visit[now] + 1
        q.append(next)
# 출력
print(visit[end]-1)