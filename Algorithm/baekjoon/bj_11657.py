import sys
inf = sys.maxsize
input = sys.stdin.readline


def bf():
    for idx in range(N):
        for now in range(1,N+1):
            for dist_next, next in graph[now]:
                if distance[now] != inf and distance[next] > distance[now] + dist_next :
                    distance[next] = distance[now] + dist_next
                    if idx + 1 == N:
                        return True


N,M = map(int,input().split())

graph =[[] for _ in range(N+1)]

for _ in range(M):
    a,b,cost = map(int,input().split())
    graph[a].append((cost,b))

distance = [inf] * (N+1)
distance[1] = 0



if bf() :
    print(-1)
else :
    for i in distance[2:]:
        if i == inf:
            print(-1)
        else :
            print(i)