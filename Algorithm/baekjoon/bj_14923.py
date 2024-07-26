from collections import deque


dr = (1,0),(0,1),(-1,0),(0,-1)

N,M = map(int,input().split())
sx,sy = map(lambda x: int(x)-1, input().split())
ex,ey = map(lambda x: int(x)-1, input().split())
arr = [[*map(int,input().split())] for _ in range(N)]

q = deque([(sx,sy,0)])
visit = [[[0,0] for _ in range(M)] for _ in range(N)]
visit[sx][sy][0]=1

while q:
    x,y, cnt = q.popleft()

    if x==ex and y==ey:
        exit(print(visit[x][y][cnt]-1))

    for dx,dy in dr:
        di,dj = x+dx, y+dy
        if 0<=di<N and 0<=dj<M:
            if not visit[di][dj][cnt]:
                if not arr[di][dj]:
                    q.append((di,dj,cnt))
                    visit[di][dj][cnt] = visit[x][y][cnt] + 1
                elif not cnt:
                    q.append((di,dj,cnt+1))
                    visit[di][dj][cnt+1] = visit[x][y][cnt] + 1
print(-1)