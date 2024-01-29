### 이상한 문제였음 ###
### 물어볼 것 ###

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
 
T = int(input())
 
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    balls = [list(map(int, input().split())) for _ in range(N)]
    max_num = 0
 
    for c in range(N):
        for r in range(M):
            hap = balls[c][r]
            for i in range(1, balls[c][r] + 1):
                for d in range(4):
                    ni, nj = c + di[d] * i, r + dj[d] * i
                    if 0 <= ni < N and 0 <= nj < M:
                        hap += balls[ni][nj]
            max_num = max(max_num, hap)
 
    print(f'#{tc} {max_num}')
 