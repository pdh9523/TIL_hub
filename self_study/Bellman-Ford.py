####

def Bellman_Ford():
    for i in range(N):                                              # 각 노드 숫자만큼 노드를 돌면서 ( O(N**2))
        for now in range(1, N+1):                                   
            for next, dist_next in graph[now]:                      # 그래프에 순회가 있는지 확인
                if distance[next] > distance[now] + dist_next :
                    distance[next] = distance[now] + dist_next
                    if i == N-1:                                    # 마지막 까지 순회가 확인된다면
                        return True                                 # 순회가 있음

    return False


N,M = map(int,input().split())          # N : 정점 M : 간선

graph = [ [] for _ in range(N+1)]       # 빈 그래프 설정

for _ in range(M):                      # 그래프 제작    
    s,e,t = map(int,input().split())
    graph[s].append((e,t))
    graph[e].append((s,t))

distance = [0] * (N+1)                  # distance 설정

print("YES" if Bellman_Ford() else "NO")

####### 타임머신
import sys

input = sys.stdin.readline


def bf():
    for idx in range(N):
        for now in range(1,N+1):
            for dist_next, next in graph[now]:
                if distance[now] != float('inf') and distance[next] > distance[now] + dist_next :
                    distance[next] = distance[now] + dist_next
                    if idx + 1 == N:
                        return True


N,M = map(int,input().split())

graph =[[] for _ in range(N+1)]

for _ in range(M):
    a,b,cost = map(int,input().split())
    graph[a].append((cost,b))

distance = [1e9] * (N+1)
distance[1] = 0



if bf() :
    print(-1)
else :
    for i in distance[2:]:
        if i == 1e9:
            print(-1)
        else :
            print(i)