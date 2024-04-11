from collections import deque
import sys

input = sys.stdin.readline

dx, dy, dz = [1, 0, -1, 0] , [0, 1, 0, -1], [-1, 0, 1]

M,N,H = map(int,input().split()) # N 세로 M 가로 H 높이
q = deque()
tomatoes = [[[]for _ in range(M)] for _ in range(N)]

for h in range(H):                                  # h : 높이 정보
    for i in range(N):                              # i : 세로
        tomato = list(map(int,input().split()))
        for j in range(M):                          # j : 가로
            tomatoes[i][j].append(tomato[j])

        for key in enumerate(tomato):               # 토마토 위치 체크
            if key[1] == 1:
                q.append([i,key[0], h])             # 저장 방식은 i , j , h

# 토마토 이동 방향 : 위 아래(h열 +/- 1), 델타(같은 h열 내에서 델타탐색)
                
max_value = 0
visit = [[[0]*H for _ in range(M)] for _ in range(N)]

while q:                                                                    # q 를 통한 bfs

    i,j,h = q.popleft()
    for dr in range(3):
        dh = h + dz[dr]
        di = i 
        dj = j
        for dt in range(4):
            if dz[dr] == 0 :                                                # dh : 높이 정보 (-1,1 또는 델타탐색)
                di = i + dx[dt]
                dj = j + dy[dt]
            if 0<= di < N and 0 <= dj < M and 0 <= dh < H:

                if visit[di][dj][dh] == 0 and tomatoes[di][dj][dh] == 0 :   
                    visit[di][dj][dh] = visit[i][j][h] + 1
                    tomatoes[di][dj][dh] = 1
                    q.append((di,dj,dh))

                    max_value = max(visit[di][dj][dh], max_value)           # 최대값 비교

for box in tomatoes:                # 토마토 박스 뭉치
    for tomato in box:              # 뭉치 > 토마토 박스
        if 0 in tomato:             # 박스 안에 토마토가 안익었으면
            exit(print(-1))         # -1
else :                          
    print(max_value)                # 아니면 0