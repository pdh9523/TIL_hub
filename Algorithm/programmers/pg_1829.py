from collections import deque

dr = (1,0),(0,1),(-1,0),(0,-1)

def Solution(m,n,picture):
    answer = [0,0]
    numberOfArea = 0
    maxSizeOfOneArea = 0
    visit = [[0]*n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if picture[i][j] !=0 and not visit[i][j]:
                target = picture[i][j]
                q = deque([(i,j)])
                visit[i][j] = 1
                cnt = 1
                while q:
                    x,y = q.popleft()

                    for dx,dy in dr:
                        di,dj = x+dx, y+dy
                        if 0<=di<m and 0<=dj<n and not visit[di][dj] and picture[di][dj]==target:
                            cnt += 1
                            visit[di][dj] = 1
                            q.append((di,dj))
                maxSizeOfOneArea = max(maxSizeOfOneArea, cnt)
                numberOfArea+=1

    answer[0] = numberOfArea
    answer[1] = maxSizeOfOneArea
    return answer

m=6
n=4
picture =[[1, 1, 1, 0], [1, 2, 2, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 3]]

print(Solution(m,n,picture))