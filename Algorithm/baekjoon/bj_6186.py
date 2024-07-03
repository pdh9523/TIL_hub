from collections import deque

dr = (1,0),(0,1),(-1,0),(0,-1)


N,M = map(int,input().split())
arr = [ list(input()) for _ in range(N) ]

cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j]==".": continue

        q = deque([(i,j)])
        arr[i][j] = "."
        while q :
            x,y = q.popleft()

            for dx,dy in dr:
                di,dj = x+dx, y+dy

                if 0<=di<N and 0<=dj<M and arr[di][dj]=="#":
                    arr[di][dj] = "."
                    q.append((di,dj))
        cnt += 1
print(cnt)