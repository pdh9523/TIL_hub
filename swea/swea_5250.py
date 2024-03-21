from heapq import *

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for idx in range(int(input())):
    # 입력
    size = int(input())
    arr = [list(map(int,input().split())) for _ in range(size)]


    # 다익스트라 
    hq = [(0,0,0)]
    distance = [[float('inf')] * size for _ in range(size)]
    distance[0][0] = 0

    while hq :                                                          
        dist_now , i , j = heappop(hq)
        
        if distance[i][j] >= dist_now:
            
            for dt in range(4):
                di = i + dx[dt]
                dj = j + dy[dt]
                if 0 <= di < size and 0 <= dj < size :
                    dist_next = max(0, arr[di][dj]-arr[i][j]) + 1       # 가중치 계산 (가려는 곳이 더 낮으면 0, 높으면 차이) + 1
                    cost = dist_now + dist_next
                    
                    if distance[di][dj] > cost:
                        distance[di][dj] = cost
                        heappush(hq,(cost,di,dj))
                        
    print(f"#{idx+1} {distance[size-1][size-1]}")