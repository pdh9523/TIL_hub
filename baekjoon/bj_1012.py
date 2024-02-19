from collections import deque
import sys

dx = [0,1,0,-1]
dy = [1,0,-1,0]

t = int(input())

for _ in range(t):
    M,N,K = map(int, sys.stdin.readline().strip("\n").split()) # M : 가로 길이, N : 세로 길이, K : 배추 개수
    farm = [[0 for _ in range(M)] for _ in range(N)] # 배추 농장
    baechu_list = [] 
    for _ in range(K):
        baechu = tuple(map(int, sys.stdin.readline().strip("\n").split()))
        n,m = baechu
        farm[m][n] = 1
        baechu_list.append(baechu)
        
    
    result = 0 
    for j,i in baechu_list:
        start = [i,j]
        cnt = 0 
        q = deque()
        q.append(start)
    

        while q :
            ti, tj = q.popleft()
            if farm[ti][tj] == 1:
                farm[ti][tj] = 0
    
                cnt += 1
            for dlt in range(4) :
                di = ti + dx[dlt]
                dj = tj + dy[dlt]
                if 0<= di < N and 0<= dj < M :
                    if farm[di][dj] == 1:
                        q.append([di,dj])
        if cnt != 0 :
            result += 1
    print(result)



###
    
    
from collections import deque
import sys

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(farm, x, y):
    queue = deque([(x, y)])
    farm[x][y] = 0
    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < N and 0 <= ny < M and farm[nx][ny] == 1:
                farm[nx][ny] = 0
                queue.append((nx, ny))

t = int(input())

for _ in range(t):
    M, N, K = map(int, sys.stdin.readline().strip().split())
    farm = [[0] * M for _ in range(N)]
    for _ in range(K):
        j, i = map(int, sys.stdin.readline().strip().split())
        farm[i][j] = 1
    
    result = 0 
    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1:
                bfs(farm, i, j)
                result += 1
    print(result)
