# 함수 없이 BFS 구현 해보기
import sys
sys.stdin = open("5105.txt")

t = int(input())

for idx in range(t) :
    size = int(input())         # 미로의 사이즈
    maze = [list(input()) for _ in range(size)]
    
    # 시작점 찾기
    for i in range(size):                       
        for j in range(size):
            if maze[i][j] == "3" :
                start = (i,j)
                break
    
    # 델타 탐색
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]


    q = [start]
    visit = [[0 for _ in range(size+1)] for _ in range(size+1)]
    # BFS 탐색 시작
    visit[start[0]][start[1]] = 1
    while q :
        tc = q.pop()
        # 도착시 
        if maze[tc[0]][tc[1]] == "2":
            print(f"#{idx+1} {visit[tc[0]][tc[1]]-2}")  # 2 앞에 도착하면 카운팅이 끝나는걸로 생각하는 듯. 그래서 -1 -1
            break
        # 도착하지 않았을 시 갈 수 있는 길을 델타 탐색으로 지정
    
        for dlt in range(4):
            di = tc[0]+dx[dlt]
            dj = tc[1]+dy[dlt]
            if 0 <= di < size and 0 <= dj < size :
                if maze[di][dj] != "1" :
                    if visit[di][dj] == 0 :
                        visit[di][dj] = visit[tc[0]][tc[1]] + 1
                        q.append((di, dj))
    else :
        print(f"#{idx+1} {0}")