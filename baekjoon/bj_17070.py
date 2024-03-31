# from collections import deque
# from time import time
# st = time()
# dx,dy=[0,1],[1,1]       # 가로 + 대각선         ( 이전 파이프가 가로인 경우)
# rx,ry=[1,1],[0,1]       # 세로 + 대각선       ( 이전 파이프가 세로인 경우)
# cx,cy=[0,1,1],[1,0,1]   # 대각선 + 가로 + 세로 (이전 파이프가 대각선인 경우)
# # 가로 0 세로 1 대각 2 로 q에 디렉션 저장
# # 사이클이 만들어지지 않으니까 visit가 필요하진 않음


# N = int(input())
# house = [list(map(int,input().split())) for _ in range(N)]

# start = (0,1,0)

# q = deque([start])
# cnt = 0
# while q :
#     i, j, dr = q.popleft()

#     if i == j == N-1 :
#         cnt += 1
#         continue

#     ### 분기를 다 나눠야하나?
    
#     # 가로 시작
#     if dr == 0 :
#         for dt in range(2):
#             di = i + dx[dt]
#             dj = j + dy[dt]
#             if 0 <= di < N and 0 <= dj < N :
#                 # 가로 -> 가로
#                 if dt == 0 :
#                     if house[di][dj] == 0 :
#                         q.append((di,dj,0))
#                 elif dt == 1 :
#                     if house[i+1][j] == house[i][j+1] == house[i+1][j+1] == 0 :
#                         q.append((di,dj,2))
    
#     # 세로 시작
#     elif dr == 1 :
#         for rt in range(2):
#             ri = i + rx[rt]
#             rj = j + ry[rt]
#             if 0 <= ri < N and 0 <= rj < N :
#                 if rt == 0 : 
#                     if house[ri][rj] == 0 :
#                         q.append((ri,rj,1))
#                 elif rt == 1 :
#                     if house[i+1][j] == house[i][j+1] == house[i+1][j+1] == 0 :
#                         q.append((ri,rj,2))
                        
#     # 대각선 시작
#     elif dr == 2 :
#         for ct in range(3):
#             ci = i + cx[ct]
#             cj = j + cy[ct]
#             if 0 <= ci < N and 0 <= cj < N :
#                 if ct == 0 :
#                     if house[ci][cj] == 0 :
#                         q.append((ci,cj,0))
#                 elif ct == 1 :
#                     if house[ci][cj] == 0 :
#                         q.append((ci,cj,1))
#                 elif ct == 2 :
#                     if house[i+1][j] == house[i][j+1] == house[i+1][j+1] == 0 :
#                         q.append((ci,cj,2))
# print(cnt)
# print(time()-st)
## 16 * 16 배열에서 10.8 초 걸림

# DP 방식 활용해야할듯

N = int(input())
house = [list(map(int,input().split())) for _ in range(N)]

# DP[i][j][dr]
# dr : 가로 0 세로 1 대각 2
DP = [[[0,0,0] for _ in range(N)] for _ in range(N)]
DP[0][1][0] = 1
# 경우의 수 찾듯이, 각 좌표의 이전 길에서 정보를 받아오기
# 정보는 가로, 세로, 대각에서 온 정보를 각각 저장하기
# 저장된 정보를 바탕으로 메모이제이션 시행
for i in range(2,N):
    if house[0][i] == 0:
        DP[0][i][0] = DP[0][i-1][0]

for i in range(1,N):
    for j in range(1,N):
        # 대각
        if house[i][j] == house[i][j-1] == house[i-1][j] == 0 :
            DP[i][j][2] = DP[i-1][j-1][2] + DP[i-1][j-1][1] + DP[i-1][j-1][0]
        # 가로, 세로 
        if house[i][j] == 0 :
            DP[i][j][0] = DP[i][j-1][0] + DP[i][j-1][2]
            DP[i][j][1] = DP[i-1][j][1] + DP[i-1][j][2]

print(sum(DP[-1][-1]))