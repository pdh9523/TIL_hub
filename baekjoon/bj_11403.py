from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs () :
    while q :
        i,j = q.popleft()
        for dt in range(4):
            di = i + dx[dt]
            dj = j + dy[dt]
            if 0 <= di < size and 0 <= dj < size:
                if arr[di][dj] and not visit[di][dj]:
                    q.append((di,dj))
                    visit[di][dj] = 1



size = int(input())

arr = [list(map(int,input().split())) for _ in range(size)]

visit = [[0] * size for _ in range(size)]

for i in range(size):
    for j in range(size):
        if arr[i][j] == 1 and not visit[i][j]:
            q = deque([(i,j)])
            bfs()
print(visit)
