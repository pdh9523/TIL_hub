import sys
from heapq import heappop, heappush

input = sys.stdin.readline

dr = (1,0),(0,1),(-1,0),(0,-1)

N,M = map(int,input().split())
arr = [[*map(int,input().split())] for _ in range(N)]
K = int(input())

hq = []
visit = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if i==0 or i==N-1 or j==0 or j==M-1:
            visit[i][j] = 1
            heappush(hq,(-arr[i][j],i,j))

while K:
    _, i,j = heappop(hq)

    print(i+1,j+1)
    K-=1
    

    for dx,dy in dr:
        di,dj = i+dx, j+dy
        if 0<=di<N and 0<=dj<M and not visit[di][dj]:
            visit[di][dj] = 1
            heappush(hq,(-arr[di][dj],di,dj))