import sys; input = sys.stdin.readline
from collections import deque


def bfs(i,j):
    q = deque([(i,j)])
    while q:
        x,y = q.popleft()

        for dx,dy in dr:
            di,dj = x+dx, y+dy
            if 0<=di<N and 0<=dj<M and arr[di][dj]:
                arr[di][dj]=0
                q.append((di,dj))
    return 1

dr = (1,0),(0,1),(-1,0),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)


N,M = map(int,input().split())
arr = [[*map(int,input().split())] for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            cnt += bfs(i,j)
print(cnt)
