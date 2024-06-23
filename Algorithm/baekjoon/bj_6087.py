from heapq import heappush, heappop
def findC():
    res = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == "C":
                res.append((i,j))
    return res

dx = [1,0,-1,0]
dy = [0,1,0,-1]

M,N = map(int,input().split())
arr = [list(input()) for _ in range(N)]
data = findC()
x,y = data[0]
xx,yy = data[1]

ans = float('inf')
for d in range(4):
    # 앞의 dist는 꺾은 횟수, d는 델타 값 (변화 시 꺾은 것)
    hq = [(0,d,x,y)]
    distance = [ [float('inf')]*M for _ in range(N) ]
    distance[x][y] = 0
    while hq:
        dist_now, dr, i, j = heappop(hq)

        if (i,j)==(xx,yy):
            ans = min(ans, dist_now)
            break 

        for dt in range(4):
            di = i+dx[dt]
            dj = j+dy[dt]
            if 0<=di<N and 0<=dj<M and arr[di][dj]!="*":
                dist_next = dist_now if dr==dt else dist_now+1
                if distance[di][dj] > dist_next:
                    distance[di][dj] = dist_next
                    heappush(hq, (dist_next, dt, di,dj))

print(ans)