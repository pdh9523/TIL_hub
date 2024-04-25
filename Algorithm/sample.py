import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


N, M, K = map(int, input().split())
place = [list(map(int, list(input().strip()))) for _ in range(N)]
visit = [ [ [0] * (K+1) for _ in range(M) ] for _ in range(N) ]

queue = deque()
queue.append([0, 0, 0])
visit[0][0][0] = 1

while queue:
    y, x, cnt = queue.popleft()
    if [y, x] == [N - 1, M - 1]:
        
        exit( print(visit[y][x][cnt]))

    for i in range(4):
        
        nx, ny = x+dx[i], y+dy[i]

        if 0 <= nx < M and 0 <= ny < N and not visit[ny][nx][cnt]:
            
            if not place[ny][nx]:
                visit[ny][nx][cnt] = visit[y][x][cnt] + 1
                queue.append([ny, nx, cnt])

            elif place[ny][nx] and cnt < K:
                visit[ny][nx][cnt+1] = visit[y][x][cnt] + 1
                queue.append([ny, nx, cnt+1])
print(-1)