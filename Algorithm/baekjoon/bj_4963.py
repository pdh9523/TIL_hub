from collections import deque

dx = [1,0,-1,0,1,1,-1,-1]
dy = [0,1,0,-1,-1,1,-1,1]

N,M = map(int,input().split())  # N 가로 M 세로
while N != 0 :
    land = [list(map(int,input().split())) for _ in range(M)]


    cnt = 0
    visit = [[0] * N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            if land[i][j] == 1 and not visit[i][j]:
                q = deque([(i,j)])
                while q:
                    x,y = q.popleft()

                    for dt in range(8):
                        di = x + dx[dt]
                        dj = y + dy[dt]
                        if 0 <= di < M and 0 <= dj < N:
                            if land[di][dj] == 1 and not visit[di][dj] :
                                visit[di][dj] = 1
                                q.append((di,dj))
                cnt += 1
    print(cnt)

    N,M = map(int,input().split())