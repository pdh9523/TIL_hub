from collections import deque


dx,dy = [1,-1,0,0], [0,0,-1,1]

N,M = map(int,input().split()) # N 세로 M 가로

islands = [list(input()) for _ in range(N)]

ans = 0 
for i in range(N):
    for j in range(M):
        if islands[i][j] == "L" : 
            visit = [ [-1]*M for _ in range(N) ]
            q = deque([(i,j)])
            visit[i][j] = 0
            tmp = 0
            while q : 
                x,y = q.popleft()

                for dt in range(4):
                    di = x + dx[dt]
                    dj = y + dy[dt]
                    if 0 <= di < N and 0 <= dj < M :
                        if visit[di][dj] == -1 and islands[di][dj] == "L" :
                            visit[di][dj] = visit[x][y] + 1
                            tmp = max(visit[di][dj],tmp)
                            q.append((di,dj))
            ans = max(ans,tmp)
print(ans)