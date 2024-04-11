from collections import deque

dx = [2,1,-2,-1,2,-1,-2,1]
dy = [1,2,-1,-2,-1,2,1,-2]


for _ in range(int(input())):

    size = int(input())
    chess = [[0] * size for _ in range(size)]

    # ki,kj = 나이트 좌표 (1)
    ki,kj = list(map(int,input().split()))
    chess[ki][kj] = 1

    # ti,tj = 목표 좌표 (2)
    ti,tj = list(map(int,input().split()))
    chess[ti][tj] = 2

    visit = [[0] * size for _ in range(size)]
    q = deque([(ki,kj)])
    visit[ki][kj] = 0
    
    while q:
        i,j = q.popleft()

        if (i,j) == (ti,tj):
            print(visit[i][j])
            break
        for dt in range(8):
            di = i + dx[dt]
            dj = j + dy[dt]
            if 0 <= di < size and 0 <= dj < size:
                if not visit[di][dj] :
                    visit[di][dj] = visit[i][j] + 1
                    q.append((di,dj))
