import sys; input=sys.stdin.readline
from collections import deque


dr = (-1,0),(-1,1),(0,1),(1,1),(1,0),(0,-1)
er = (-1,-1),(-1,0),(0,1),(1,0),(1,-1),(0,-1)

N,M,K = map(int,input().split())
arr = [[True] * M for _ in range(N)]

for _ in range(K):
    a,b = map(int,input().split())
    arr[a][b] = False

visit = [[0] * M for _ in range(N)]
q = deque([(0,0)])
visit[0][0] = 1
while q:
    x,y = q.popleft()

    if x == N-1 and y == M-1:
        exit(print(visit[x][y]-1))
    d = dr if x%2 else er
    for dx,dy in d:
        di,dj = x+dx, y+dy
        if 0<=di<N and 0<=dj<M and not visit[di][dj] and arr[di][dj]:
            visit[di][dj] = visit[x][y] + 1
            q.append((di,dj))

print(-1)