import sys
from collections import deque

input = sys.stdin.readline

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

N, M = map(int, input().split())  # N 세로 M 가로

arr = [list(map(int, list(input().strip()))) for _ in range(N)]
end = N - 1, M - 1

# 0: 벽을 부수지 않고 방문, 1: 벽을 부수고 방문
visit = [[[False, False] for _ in range(M)] for _ in range(N)]
visit[0][0][0] = True  # 시작점 방문 표시

q = deque([(0, 0, False)])  # 초기 위치와 벽 부수기 여부(False: 아직 부수지 않음)
while q:
    i, j, chance = q.popleft()

    if (i, j) == end:
        exit(print(int(visit[i][j][chance])))
    for dt in range(4):
        di = i + dx[dt]
        dj = j + dy[dt]
        if 0 <= di < N and 0 <= dj < M:
            if not visit[di][dj][chance]:
                if arr[di][dj] == 0:
                    q.append((di, dj, chance))
                    visit[di][dj][chance] = visit[i][j][chance] + 1
                elif not chance:  # 벽을 아직 부수지 않았다면
                    q.append((di, dj, True))
                    visit[di][dj][1] = visit[i][j][0] + 1
else:
    print(-1)
