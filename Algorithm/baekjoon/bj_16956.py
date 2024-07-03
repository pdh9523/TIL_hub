dr = (1,0),(0,1),(-1,0),(0,-1)

N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] != "W": continue
            
        for dx,dy in dr:
            di,dj = i+dx, j+dy
            if 0<=di<N and 0<=dj<M:
                if arr[di][dj] == ".":
                    arr[di][dj] = "D"
                elif arr[di][dj] == "S":
                    exit(print(0))
print(1)
for row in arr:
    print(*row, sep="")