import sys; input = sys.stdin.readline


dr = (1,0),(0,1),(-1,0),(0,-1)

def dfs():
    stack = [start]
    visit = [[False]*M for _ in range(N)]
    
    while stack:
        x,y = stack.pop()
        if arr[x][y] == "L":
            return False
        if visit[x][y]: continue
        visit[x][y] = True
            
        for dx,dy in dr:
            di,dj = x+dx, y+dy
            if 0 <= di < N and 0 <= dj < M: 
                if not visit[di][dj] and arr[di][dj] != "X":
                    stack.append((di,dj))
    
    return True


def ice_braking():
    for x in range(N):
        for y in range(M):
            if arr[x][y] == ".":
                for dx,dy in dr:
                    di,dj = x+dx, y+dy
                    if 0 <= di < N and 0 <= dj < M:
                        if arr[di][dj] == "X":
                            arr[di][dj] = ".."
    for x in range(N):
        for y in range(M):
            if arr[x][y] == "..":
                arr[x][y] = "."


def find():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == "L":
                arr[i][j] = "."
                return (i,j)


N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
start = find()

cnt = 0 
while dfs():
    cnt += 1
    ice_braking()

print(cnt)

## 공간에 대한 bfs로 접근해야 할 듯

