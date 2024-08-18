from collections import deque

dr = (1,0),(0,1),(-1,0),(0,-1)

N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]

q = deque([(0,0)])
visit = [[0]*M for _ in range(N)]
visit[0][0] = 1
while q:
    x,y = q.popleft()

    if x==N-1 and y==M-1:
        exit(print(visit[x][y]))
    
    for dx,dy in dr:
        di,dj = x+dx, y+dy
        if 0<=di<N and 0<=dj<M:
            if visit[di][dj]: continue
            if arr[x][y] =="0": continue

            visit[di][dj] = visit[x][y]+1
            q.append((di,dj))