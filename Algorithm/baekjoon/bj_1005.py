import sys
from collections import deque

input = sys.stdin.readline

# 위상정렬, Topological Sort 
# 유향 그래프의 노드들을 간선의 방향을 거스르지 않는 선에서,
# 선후 관계에 따라 정렬하기 위한 정렬 방식.

for _ in range(int(input())):
    N,K = map(int,input().split())                              # N: 건물 개수 K: 노드 개수
    time = [0] + list(map(int,input().split()))                 # 각 인덱스의 건물 건설 소요 시간
    graph = [ [] for _ in range(N+1) ]                          # 건물 간 관계 그래프
    degree = [0] * (N+1)                                        # 각 건물의 진입 차수 리스트
    
    for _ in range(K):
        a,b = map(int,input().split())
        graph[a].append(b)
        degree[b] +=1                                           # 그래프를 만드는 것 처럼 하되, 뒤의 노드의 진입 차수를 한칸씩 올려 표기해둔다.

    DP = [0] * (N+1)
    q = deque()
    for i in range(1,N+1):
        if degree[i] == 0 :                                     # 진입 차수가 0 인 정점에 대해서
            q.append(i)                                         # q에 담아 순회를 준비한다.
            DP[i] = time[i]                                     # DP에 각 건물의 건설 소요 시간을 담아둔다.

    print(degree)
    # 위상 정렬                
    while q :
        now = q.popleft()                                       

        for next in graph[now]:                                 # 현재 탐색 중인 정점에서 선택 가능한 노드들에 대해서
            degree[next] -= 1                                   # 진입차수를 한칸씩 빼고,
            DP[next] = max(DP[now]+time[next], DP[next])        # DP를 계산한다 
            # 현재 건물까지 계산된 총 비용 + 다음 건물 소요 비용 vs 계산된 다음 건물까지 계산된 총 비용

            if degree[next] == 0 :                              # 바로 진입할 수 있을 정도로 깊이 탐색 중이라면
                q.append(next)                                  # q에 더해 탐색한다. 

    print(DP[(int(input()))])                                   # 마지막 W 값을 받아 DP에서 출력한다.