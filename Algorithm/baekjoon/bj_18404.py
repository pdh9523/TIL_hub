import sys; input=sys.stdin.readline
from collections import deque


dr = (2,1),(2,-1),(1,2),(1,-2),(-2,1),(-2,-1),(-1,-2),(-1,2)

N,M = map(int,input().split())
i,j = map(lambda x: int(x)-1,input().split())
q = deque([(i,j)])

visit = [[0]*N for _ in range(N)]
visit[i][j] = 1
ans = []
while q: 
    x,y = q.popleft()

    for dx,dy in dr:
        di,dj = x+dx, y+dy
        if 0<=di<N and 0<=dj<N:
            if visit[di][dj]: continue
            visit[di][dj] = visit[x][y]+1
            q.append((di,dj))

for _ in range(M):
    a,b = map(lambda x: int(x)-1,input().split())
    ans.append(visit[a][b]-1)
print(*ans)