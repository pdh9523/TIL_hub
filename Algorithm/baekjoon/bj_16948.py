from collections import deque

dr = (-2,-1),(-2,1),(0,-2),(0,2),(2,-1),(2,1)

N = int(input())
i,j,x,y = map(int,input().split())

visit = dict()
visit[(i,j)]=0
q = deque([(i,j)])
while q:
    i,j = q.popleft()
    if (i,j)==(x,y):
        exit(print(visit[(x,y)]))

    for dx,dy in dr:
        di,dj = i+dx,j+dy
        if 0 <= di < N and 0 <= dj < N:
            if not visit.get((di,dj)):
                visit[(di,dj)]=visit[(i,j)]+1
                q.append((di,dj))
print(-1)