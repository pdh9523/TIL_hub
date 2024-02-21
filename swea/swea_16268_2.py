T = int(input())

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for idx in range(T):
    N,M = map(int,input().split())
    ballons = [list(map(int,input().split())) for _ in range(N)]
    result = 0
    for i in range(N):
        for j in range(M):
            s = ballons[i][j]
            for dt in range(4):
                di = i+dx[dt]
                dj = j+dy[dt]
                if 0<= di < N and 0<= dj < M:
                    s += ballons[di][dj]
            if s > result:
                result = s
    print(f"#{idx+1} {result}")