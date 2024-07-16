import sys
from collections import deque

input = sys.stdin.readline

def find():
    for i in range(N):
        for j in range(N):
            if arr[i][j] =="F":
                return i,j

dr = (-1,0),(0,-1),(0,1),(1,-1),(-1,1),(-1,-1),(1,-1),(1,1)

N = int(input())
arr = [list(input()) for _ in range(N)]

i,j = find()
q = deque([(i,j)])
visit = [[0]*N for _ in range(N)]
visit[i][j] = 1

ans = 0
while q:
    x,y = q.popleft()

    for dx,dy in dr:
        di,dj = x+dx,y+dy
        if 0<=di<N and 0<=dj<N and not visit[di][dj] and arr[di][dj] ==".":
            q.append((di,dj))
            ans += 1
            visit[di][dj] = 1
    
print(ans)