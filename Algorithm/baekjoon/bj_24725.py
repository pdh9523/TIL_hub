dr = (1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)

N,M = map(int,input().split())

arr = [list(input()) for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] in ("I","E"):
            for dx,dy in dr:
                di,dj = i+dx,j+dy
                if 0<=di<N and 0<=dj<M and arr[di][dj] in ("N","S"):
                    di,dj = di+dx, dj+dy
                    if 0<=di<N and 0<=dj<M and arr[di][dj] in ("T","F"):
                        di,dj = di+dx, dj+dy
                        if 0<=di<N and 0<=dj<M and arr[di][dj] in ("P","J"):
                            cnt += 1
print(cnt)