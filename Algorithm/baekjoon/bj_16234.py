import sys
from collections import deque

input =sys.stdin.readline



dr = ((1,0),(0,1),(-1,0),(0,-1))
N,L,R = map(int,input().split())

arr = [ [*map(int,input().split())] for _ in range(N) ]
ans = 0 
check = False

while True :
    if check :
        break

    check = True

    visit = [ [0]*N for _ in range(N) ]

    for i in range(N):
        for j in range(N):
            if visit[i][j] : continue
            
            q = deque([(i,j)])

            visit[i][j] = 1
            cnt = 1
            temp = [(i,j)]
            tmp = arr[i][j]
            while q :
                x,y = q.popleft()
            
                for dx,dy in dr:
                    di,dj = x+dx, y+dy

                    if not(0 <= di < N and 0 <= dj < N) or visit[di][dj]: continue
                    if L<=abs(arr[x][y]-arr[di][dj])<=R:
                        visit[di][dj] = 1
                        q.append((di,dj))
                        tmp += arr[di][dj]
                        cnt += 1
                        check = False
                        temp.append((di,dj))
            for x,y in temp :
                arr[x][y] = tmp//cnt

    if not check :
        ans += 1
print(ans)