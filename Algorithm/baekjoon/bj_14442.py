import sys
from collections import deque

input = sys.stdin.readline

dx, dy = [1,0,-1,0],[0,1,0,-1]

N,M,K = map(int,input().split())    # N 세로 M 가로 K 벽꿍
maze = [list(map(int,list(input().strip()))) for _ in range(N)]


start = (0,0,K)
q = deque([start])
visit = [[[0,K] for _ in range(M)] for _ in range(N)]   # visit[i][j][0] : 방문 처리 / visit[i][j][1] : 기회 저장
visit[0][0][0] = 1

while q :
    i,j,k = q.popleft()

    if i == N-1 and j == M-1 :
        print(visit[i][j][0])
        break

    for dt in range(4):
        di = i + dx[dt]
        dj = j + dy[dt]
        if 0 <= di < N and 0 <= dj < M :
            # 일반 길
            if not maze[di][dj]:
                if not visit[di][dj][0] or k > visit[di][dj][1]: #방문하지 않았거나,  방문했는데 뚫기 회수가 더 많은 경우
                    q.append((di,dj,k))
                    visit[di][dj][0] = visit[i][j][0]+1
                    visit[di][dj][1] = k
            # 벽인데 기회가 있는 경우
            elif k and maze[di][dj]:
                if not visit[di][dj][0] or k-1 > visit[di][dj][1]:
                    q.append((di,dj,k-1))
                    visit[di][dj][0] = visit[i][j][0]+1
                    visit[di][dj][1] = k-1
else :
    print(-1)