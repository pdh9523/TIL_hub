from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for t in range(int(input())):
    size = int(input())
    arr = [list(map(int,input().split())) for _ in range(size)]
    visit = [[0]*size for _ in range(size)]
    ans = (1000001,0)
    for i in range(size):
        for j in range(size):
            if visit[i][j] == 0 :
                s = (i,j)
                q = deque([s])
                cnt = 1
                while q :
                    i,j = q.popleft()
                    for dt in range(4):
                        di = i + dx[dt]
                        dj = j + dy[dt]
                        if 0 <= di < size and 0 <= dj < size:
                            if arr[di][dj]-arr[i][j] == 1:
                                q.append((di,dj))
                                visit[di][dj] = 1
                                cnt +=1
                if cnt > ans[1]:
                    ans = (arr[s[0]][s[1]], cnt)
                elif cnt == ans[1]:
                    ans = (min(ans[0],arr[s[0]][s[1]]), cnt)
    print(f"#{t+1}",*ans)