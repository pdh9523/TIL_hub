import sys
from collections import deque

input = sys.stdin.readline

dx, dy = [1,0,-1,0], [0,1,0,-1]

N,M= map(int,input().split())   # N = 가로, M = 세로
tomatoes = []
q = deque()

for idx in range(M):
    tomato = list(map(int,input().split()))
    tomatoes.append(tomato)

    # 익은 토마토 들어있는 인덱스 추출
    for key in enumerate(tomato):
        if key[1] == 1:
            q.append((idx,key[0]))

# BFS 및 max_value 계산
visit = [[0] * (N+1) for _ in range(M)]
max_value = 0
while q :
    i,j = q.popleft()    
    for dt in range(4):
        di = i + dx[dt]
        dj = j + dy[dt]

        if 0 <= di < M and 0 <= dj < N :
            if visit[di][dj] == 0 and tomatoes[di][dj] == 0:
                visit[di][dj] = visit[i][j]+1
                tomatoes[di][dj] = 1
                q.append((di,dj))

                if visit[di][dj] > max_value :
                    max_value = visit[di][dj]

# 출력 파트
for tomato in tomatoes:
    if 0 in tomato:
        exit(print(-1))

else :
    print(max_value)