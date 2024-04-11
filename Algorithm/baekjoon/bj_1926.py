from collections import deque

dx,dy=[1,0,-1,0],[0,1,0,-1]


def bfs (i,j) :
    cnt = 0 
    q = deque([(i,j)])
    drawings[i][j] = 0 
    cnt += 1
    while q :
        i,j = q.popleft()
        
        for dt in range(4):
            di = i + dx[dt]
            dj = j + dy[dt]
            if 0 <= di < N and 0 <= dj < M :
                if drawings[di][dj]:
                    drawings[di][dj] = 0
                    cnt += 1
                    q.append((di,dj))
    return cnt

N,M = map(int,input().split())

drawings = [list(map(int,input().split())) for _ in range(N)]

cnt = 0 
max_value = 0
for i in range(N):
    for j in range(M):
        if drawings[i][j] :
            tmp = bfs(i,j)
            max_value = max(max_value,tmp)
            cnt += 1
print(cnt)
print(max_value)