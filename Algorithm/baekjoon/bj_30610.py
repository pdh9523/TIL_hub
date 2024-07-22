import sys
from collections import deque
input = sys.stdin.readline


def bfs(i,j):
    q = deque([(i,j)])
    arr[i][j] = 0
    cnt = 1
    while q:
        x,y = q.popleft()

        for dx,dy in dr:
            di,dj = x+dx, y+dy
            if 0<=di<N and 0<=dj<M and arr[di][dj]:
                arr[di][dj] = 0
                q.append((di,dj))
                cnt += 1
    return cnt


dr = (1,0),(0,1),(-1,0),(0,-1)
N, M = map(int, input().split())
arr = [[*map(int, list(input().strip()))] for _ in range(N)]

ans = list()
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            ans.append(bfs(i,j))

print(len(ans))
print(*sorted(ans))
