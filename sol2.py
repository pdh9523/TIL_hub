from collections import deque
from pprint import pprint
dx,dy = [0,1],[1,0]

# 백트래킹 : 각 좌표에서 시간여행한 최대값을 tmp에 저장
def backtrack(i,j, result, idx=0):
    global tmp
    if idx == T :
        tmp = max(tmp,result)
        return
    
    for rt in range(2):
        di = i + dx[rt]
        dj = j + dy[rt]
        if 0 <= di < N and 0 <= dj < N :
            backtrack(di,dj,result+mine[di][dj],idx+1)
        else : 
            tmp = max(tmp,result)
            return

# 입력
N,T = map(int,input().split())
mine = [list(map(int,input().split())) for _ in range(N)]

# BFS
start = (0,0)

q = deque([start])
visit = [[[0,0] for _ in range(N)]  for _ in range(N)]
visit[0][0][0] = mine[0][0]

while q :
    i, j = q.popleft()
    for dt in range(2):
        di = i + dx[dt]
        dj = j + dy[dt]

        if 0 <= di < N and 0 <= dj < N :
            # 지나가는 조건에 한해 백트래킹 후 비교
            tmp = -float('inf')
            backtrack(di,dj,mine[di][dj])

            # 일반적인 경우 : 백트래킹의 이전에 지나온 값과 현재 값과 비교
            if visit[di][dj][0] == 0 or visit[i][j][0] + mine[di][dj] > visit[di][dj][0]:
                visit[di][dj][0] = visit[i][j][0] + mine[di][dj]
                visit[di][dj][1] = max(visit[i][j][1],tmp)
                q.append((di,dj))

            # 같은 경우 : 백트래킹의 이전에 지나온 값, 이미 저장된 값을 비교
            elif visit[i][j][0] + mine[di][dj] == visit[di][dj][0]:
                visit[di][dj][0] = visit[i][j][0] + mine[di][dj]
                visit[di][dj][1] = max(visit[di][dj][1],visit[i][j][1])
                q.append((di,dj))

pprint(visit)
print(sum(visit[-1][-1]))