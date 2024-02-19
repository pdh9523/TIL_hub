from pprint import pprint as print
size_i, size_j = map(int, input().split())         # 미로의 사이즈
maze = [list(input()) for _ in range(size_i)]



# 델타 탐색
di = [0,1,0,-1]
dj = [1,0,-1,0]


q = [(0,0)]

visit = [[0 for _ in range(size_j+1)] for _ in range(size_i+1)]
# BFS 탐색 시작
visit[0][0] = 1

while q :
    tc = q.pop(0)
    # 도착시 
    if tc == (size_i,size_j):
        break
    # 도착하지 않았을 시 갈 수 있는 길을 델타 탐색으로 지정

    for dlt in range(4):
        delta_i = tc[0]+di[dlt]
        delta_j = tc[1]+dj[dlt]
        if 0 <= delta_i < size_i and 0 <= delta_j < size_j :
            if maze[delta_i][delta_j] != "0" :
                if visit[delta_i][delta_j] == 0 :
                    visit[delta_i][delta_j] = visit[tc[0]][tc[1]] + 1
                    q.append((delta_i, delta_j))

# 도착시 
print(visit[size_i-1][size_j-1])