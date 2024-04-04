from collections import deque
from pprint import pprint
dx = [1,0,-1,0]
dy = [0,1,0,-1]

N,M = map(int,input().split())

block = [list(map(int, input().split())) for _ in range(N)]

ans = 0
## 큰 블록 찾는 과정 (tmp : 큰 블록, max_value : 점수 합)
while True :
    max_value = 0
    for i in range(N):
        for j in range(N):
            if block[i][j] != "" and block[i][j] > 0 :
                q = deque([(i,j)])
                visit = [[0] * N for _ in range(N)]
                cnt = 0 
                while q :
                    x,y = q.popleft()
                    for dt in range(4):
                        di = x + dx[dt]
                        dj = y + dy[dt]
                        if 0 <= di < N and 0 <= dj < N :
                            if not visit[di][dj] :
                                if block[i][j] == block[di][dj] or block[di][dj] == 0:
                                    q.append((di,dj))
                                    visit[di][dj] = 1
                                    cnt += 1
                if cnt > max_value :
                    max_value = cnt
                    tmp = (i,j)
    if max_value > 1 :
        print(max_value,tmp)
        ans += max_value **2
    else :
        break
    # 블록 제거하기
    i,j = tmp
    q = deque([tmp])
    col = block[i][j]
    block[i][j] = ""
    while q :
        i , j = q.popleft()
        for dt in range(4):
            di = i + dx[dt]
            dj = j + dy[dt]
            if 0 <= di < N and 0 <= dj < N :
                if block[di][dj] == 0 or block[di][dj] == col :
                    block[di][dj] = ""
                    q.append((di,dj))

    # 중력 작용하기
    
    ### 여기 만들어야합니다.


    # 뒤집기
    block = [list(char) for char in zip(*block)][::-1]

    
    pprint(block)
print(ans)