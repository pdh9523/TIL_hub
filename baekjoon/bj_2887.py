from sys import stdin
from heapq import heappop, heappush

input = stdin.readline

X,Y,Z = [],[],[]

N = int(input())
# 좌표를 따로따로 저장
for i in range(N):
    x,y,z = map(int,input().split())
    X.append((x,i))
    Y.append((y,i))
    Z.append((z,i))
# 셋다 정렬
X.sort(); Y.sort(); Z.sort()

graph = [[] for _ in range(N)]
for lst in X,Y,Z:
    for i in range(1,N):
        w1, a = lst[i-1]
        w2, b = lst[i]
        graph[a].append((abs(w1-w2),b))
        graph[b].append((abs(w1-w2),a))

hq = [(0,0)]

visit = [True] * N

ans = 0
while hq : 
    dist_now, now = heappop(hq)

    if visit[now]:
        visit[now] = False
        ans += dist_now

        for next in graph[now]:
            heappush(hq,next)
print(ans)