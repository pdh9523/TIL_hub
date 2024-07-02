from heapq import heappush, heappop

dx = 1, 0,-1 , 0
dy = 0, 1, 0 ,-1

# 찾기
def find():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == "#":
                return i,j


N = int(input())
arr = [list(input()) for _ in range(N)]
# 시작 지점 저장 
i,j = find()

hq = []
# 시작 방향 저장
for dt in range(4):
    di,dj = i+dx[dt], j+dy[dt]
    if 0<=di<N and 0<=dj<N and arr[di][dj] != "*" :
        hq.append((0,i,j,dt))
distance = [[float('inf')] * N for _ in range(N)]
distance[i][j] = 0

while hq :
    dist_now, x,y, d = heappop(hq)

    if dist_now > distance[x][y] : continue
    
    di,dj = x,y
    while True:
        di,dj = di+dx[d%4], dj+dy[d%4]
        if not (0<=di<N and 0<=dj<N) : break
        if arr[di][dj] != ".": break

    if not (0<=di<N and 0<=dj<N) : continue

    if arr[di][dj]=="#":
        ai,aj = di,dj
        distance[di][dj] = min(distance[di][dj], dist_now)

    if arr[di][dj]=="!":
        if distance[di][dj] > dist_now + 1:
            distance[di][dj] = dist_now + 1
        heappush(hq, (dist_now+1, di,dj, d+1))
        heappush(hq, (dist_now+1, di,dj, d-1))
        heappush(hq, (dist_now  , di,dj, d  ))

print(distance[ai][aj])