from collections import deque


def find_ball(color):
    for i in range(N):
        for j in range(M):
            if arr[i][j] == color:
                return i,j

def move(dir, x,y):
    dx,dy = dr[dir]
    while arr[x][y] != "#":
        di,dj = x+dx, y+dy

        if arr[di][dj] == "O":
            break

        if 0<=di<N and 0<=dj<M:
            x,y = di,dj

    return dx,dy

def bfs(bx,by, rx,ry):
    q = deque([bx,by, rx,ry])

    while q:
        bx,by, rx,ry = q.popleft()

        if arr[bx][by] == "O": continue
        if arr[rx][ry] == "O": return 
    return

dr = (1,0), (0,1), (-1,0), (0,-1)

N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]

bx,by = find_ball("B")
rx,ry = find_ball("R")

visit = [[0]*M for _ in range(N)]
visit[rx][ry] = 1

print(bfs(bx,by, rx,ry))