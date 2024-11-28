import sys; input = sys.stdin.readline


dr = (1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)

N = int(input())
arr = [list(input()) for _ in range(N)]

ans = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if arr[i][j] == ".": continue

        ans[i][j] = "*"
        for di,dj in dr:
            x,y = i+di, j+dj
            if 0<=x<N and 0<=y<N and type(ans[x][y]) == int:
                ans[x][y] += int(arr[i][j])
                if ans[x][y] >= 10: ans[x][y] = "M"
for a in ans:
    print(*a, sep="")