from collections import deque 

dx = [1,0,-1,0]
dy = [0,1,0,-1]

N,M = map(int,input().split())

glacier = []

target = set()

for _ in range(N):
    ice = list(map(int,input().split()))
    target.update(ice)
    glacier.append(ice)


ans = 0
year = -1
while True :
    year += 1
    cnt = 0
    visit = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            
            if glacier[i][j] > 0 and not visit[i][j]:
                q = deque([(i,j)])
                visit[i][j] = 1
                
                while q :
                    
                    x,y = q.popleft()

                    for dt in range(4):
                        di = x + dx[dt]
                        dj = y + dy[dt]
                    
                        if 0 <= di < N and 0 <= dj < M :
                            if not visit[di][dj] and glacier[di][dj] > 0 :
                                visit[di][dj] = 1
                                q.append((di,dj))
                cnt += 1
    if ans != cnt:
        if ans == 0 :
            ans = cnt
        elif cnt == 0 :
            exit(print(0))
        elif ans != cnt :
            exit(print(year))
        
    iceberg = [row[:] for row in glacier]
    for p in range(N):
        for q in range(M):
            for dt in range(4):
                dp = p + dx[dt]
                dq = q + dy[dt]
                if 0 <= dp < N and 0 <= dq < M :
                    if iceberg[dp][dq] == 0 and iceberg[p][q] !=0:
                        if glacier[p][q] >0:
                            glacier[p][q] -=1