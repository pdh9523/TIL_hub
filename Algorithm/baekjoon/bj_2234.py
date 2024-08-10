import sys
input = sys.stdin.readline 

def dfs():
    tmp = 0 
    stack = [(i,j)]
    while stack:
        x,y = stack.pop()
        if visit[x][y]: continue
        visit[x][y] = cnt
        tmp += 1
        for b in range(4):
            if not arr[x][y]&1<<b:
                dx,dy = dr[b]
                di,dj = x+dx,y+dy
                if not visit[di][dj]:
                    stack.append((di,dj))
    data[cnt]=tmp
    return tmp

dr = (0,-1),(-1,0),(0,1),(1,0)

M,N = map(int,input().split())
arr = [[*map(int,input().split())] for _ in range(N)]

visit =  [[0]*M for _ in range(N)]
data = dict()
cnt = 0
max_v = 0
for i in range(N):
    for j in range(M):
        if not visit[i][j]:
            cnt += 1
            max_v = max(max_v, dfs())

max_s = 0
for i in range(N):
    for j in range(M):
        for dx,dy in dr:
            di,dj = i+dx,j+dy
            if 0<=di<N and 0<=dj<M:
                if visit[i][j] == visit[di][dj]: continue
                max_s=max(max_s, data[visit[i][j]]+data[visit[di][dj]])

print(cnt)
print(max_v)
print(max_s)