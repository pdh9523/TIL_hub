import sys
input = sys.stdin.readline

def dfs(x,y):
    global cnt
    if y==M-1:
        cnt += 1
        return True
    
    for dx,dy in dr:
        di,dj = x+dx, y+dy
        if 0<=di<N and 0<=dj<M and arr[di][dj] ==".":
            arr[di][dj] = "x"
            if dfs(di,dj):    return True
    return False

dr = (-1,1),(0,1),(1,1)
N,M = map(int,input().split())
arr = [list(input().strip()) for _ in range(N)]

cnt = 0
for i in range(N):
    dfs(i,0)
print(cnt)