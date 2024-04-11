from heapq import *

dx,dy = [0,1,0,-1], [1,0,-1,0]

# 입력
N,M = map(int,input().split())  # N : 가로, M : 세로
maze = [list(map(int,list(input()))) for _ in range(M)]
# 처리

q = [(0,0,0)]
distance = [[float('inf')] * N for _ in range(M)]
distance[0][0] = 0

while q:
    dist_now,i,j = heappop(q)

    if distance[i][j] >= dist_now :

        for dt in range(4) :
            di = i + dx[dt]
            dj = j + dy[dt]
            if 0 <= di < M and 0 <= dj < N :
                cost = dist_now + maze[di][dj]
                if distance[di][dj] > cost:
                    distance[di][dj] = cost
                    heappush(q, (cost,di,dj))
print(distance[M-1][N-1])
