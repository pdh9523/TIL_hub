from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

N,M = map(int,input().split())  # N 세로 / M 가로
maze = []
for i in range(N):
    arr = list(map(int,input().split()))
    maze.append(arr)
    if 2 in arr :
       s = (i, arr.index(2))

visit = [[0] * M for _ in range(N)]
 
q = deque([s])

while q :
    
    i,j = q.popleft()

    for dt in range(4):
        di = i + dx[dt]
        dj = j + dy[dt]
        if 0<= di < N and 0 <= dj < M :
            if (visit[di][dj] == 0 or visit[di][dj] > visit[i][j] + 1) and maze[di][dj] == 1:
                visit[di][dj] = visit[i][j] + 1
                q.append((di,dj))

for i in range(N):
    for j in range(M):
        if visit[i][j] == 0 and maze[i][j] == 1:
            visit[i][j] = -1
            
for vst in visit:
    print(*vst)