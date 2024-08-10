from collections import deque

dr = (1,0),(0,1),(-1,0),(0,-1)

N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]

sheep,wolf=0,0

for i in range(N):
    for j in range(M):
        tmps, tmpw = 0,0
        if arr[i][j] != "#":
            q = deque([(i,j)])
            if arr[i][j] == "o":
                tmps += 1
            elif arr[i][j] == "v":
                tmpw += 1
            arr[i][j] = "#"
            while q:
                x,y = q.popleft()

                for dx,dy in dr:
                    di,dj = x+dx, y+dy
                    if 0<=di<N and 0<=dj<M and arr[di][dj] != "#":
                        if arr[di][dj] == "o":
                            tmps += 1
                        elif arr[di][dj] == "v":
                            tmpw += 1
                        arr[di][dj] = "#"
                        q.append((di,dj))

            if tmps>tmpw:
                sheep += tmps
            else:
                wolf += tmpw
print(sheep,wolf)