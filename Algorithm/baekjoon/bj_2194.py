import sys
from collections import deque

input = sys.stdin.readline


def is_inrange(x,y):
    for i in range(A):
        for j in range(B):
            if 0<=x+i<N and 0<=y+j<M and not arr[x+i][y+j]:
                pass
            else:
                return False
    return True

def intinput(x):
    return int(x)-1


dr = (0,1),(1,0),(0,-1),(-1,0)

N,M,A,B,K = map(int,input().split())
arr = [[0]*M for _ in range(N)]

for _ in range(K):
    i,j = map(intinput,input().split())
    arr[i][j] = 1

si,sj = map(intinput,input().split())
ei,ej = map(intinput,input().split())

q = deque([(si,sj)])

visit = [[0]*M for _ in range(N)]
visit[si][sj] = 1
while q:
    x,y = q.popleft()

    if x==ei and y==ej:
        exit(print(visit[x][y]-1))

    for dx,dy in dr:
        di,dj = x+dx,y+dy

        if is_inrange(di,dj) and not visit[di][dj]:
            q.append((di,dj))
            visit[di][dj] = visit[x][y] + 1
print(-1)