N,M = map(int,input().split())
arr = [[*map(int,list(input()))] for _ in range(N)]

stack = [(0,x) for x in range(M) if arr[0][x] == 0]

while stack :
    x,y = stack.pop()
    if x == N-1: exit(print("YES"))

    if arr[x][y]: continue

    arr[x][y] = 2
    for dx,dy in (1,0), (0,1), (-1,0), (0,-1):
        di,dj = x+dx, y+dy
        if 0 <= di < N and 0 <= dj < M and arr[di][dj]==0:
            stack.append((di,dj))
print("NO")