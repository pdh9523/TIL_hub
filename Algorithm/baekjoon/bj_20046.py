import sys
from heapq import heappop, heappush

input = sys.stdin.readline

dr = ((1,0),(0,1),(-1,0),(0,-1))

N,M = map(int,input().split())
roads = [list(map(int,input().split())) for _ in range(N)]

if roads[0][0] == -1 or roads[-1][-1] == -1 :
    exit(print(-1))

distance = [ [float('inf')] * M for _ in range(N) ]
distance[0][0] = roads[0][0]
hq = [(roads[0][0],0,0)]

while hq :
    dist_now,i,j = heappop(hq)

    if distance[i][j] < dist_now:
        continue

    for dx,dy in dr :
        di,dj = i+dx, j+dy
        if 0 <= di < N and 0 <= dj < M and roads[di][dj] != -1:
            cost = roads[di][dj] + dist_now
            if distance[di][dj] > cost:
                distance[di][dj] = cost
                heappush(hq,(cost,di,dj))

print(distance[-1][-1] if distance[-1][-1] != float('inf') else -1)