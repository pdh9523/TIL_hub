from collections import deque

N, M = map(int, input().split())
ocean = [list(map(int, input().split())) for _ in range(N)]   # 0 : 빈칸, 1 : 아기 상어


di = [1, -1, 0, 0, 1, 1, -1, -1]
dj = [0, 0, 1, -1, 1, -1, 1, -1]

most_safe = 0
for i in range(N):
    for j in range(M):
        if ocean[i][j] == 0:   # 빈칸이면, 안전거리를 구한다.
            queue = deque([[i, j]])
            visited = [[-1] * M for _ in range(N)]
            visited[i][j] = 0
            while queue:
                y, x = queue.popleft()
                for k in range(8):
                    p, q = y+di[k], x+dj[k]
                    if 0 <= p < N and 0 <= q < M and visited[p][q] == -1:
                        if ocean[p][q] == 0:                # 비어있는 칸이라면
                            visited[p][q] = visited[y][x] + 1
                            queue.append([p, q])                 # 해당 좌표 작업 리스트에 추가
                        else:                                    # 상어가 있는 칸이라면
                            if most_safe < visited[y][x] + 1:       # 최대 안전거리 업데이트
                                most_safe = visited[y][x] + 1
                            queue = []                      # 작업 리스트를 비워서 while 문 종료시키기
                            break                           # for 문 종료
print(most_safe)