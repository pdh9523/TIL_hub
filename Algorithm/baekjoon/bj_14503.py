dx = [-1,0,1,0]
dy = [0,-1,0,1]

N,M = map(int,input().split())  # N : 세로 M : 가로

i,j,dr = map(int,input().split())
if dr == 1:
    dr = 3
elif dr == 3:           # elif 확인 철저히 할 것 
    dr = 1

room = [list(map(int,input().split())) for _ in range(N)]

cnt = 0

while True :
    if room[i][j] == 0:         # 1. 현재 칸이 아직 청소 되지 않은 경우
        room[i][j] = 2          # 1. 현재 칸을 청소한다.
        cnt += 1                # cnt : 청소하는 칸의 개수
    check = True                # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 '없는가'?
    
    for dt in range(4):
        di = i + dx[dt]
        dj = j + dy[dt]

        if 0 <= di < N and 0 <= dj < M :    # 갈 수 있는 곳 중
            if room[di][dj] == 0:           # 3. 청소 안 한 곳이 있다면 
                check = False               # 빈칸이 없지 않음을 표시
                dr += 1                     # 3. 반시계 방향으로 회전한다. 
                ri = i + dx[dr%4]           # 바라보는 방향을 기준으로
                rj = j + dy[dr%4]
                if room[ri][rj] == 0:       # 3-2. 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한칸 전진한다.
                    i,j= ri,rj              
                    break

    if check :                  # 2. 빈 칸이 없다면
        i-= dx[dr%4]            # 후진한다.
        j-= dy[dr%4]
    if room[i][j] == 1:         # 2-2. 벽이라 후진할 수 없다면
        exit(print(cnt))        # 종료한다.