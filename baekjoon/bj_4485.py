from heapq import *

dx = [1,0,-1,0]
dy = [0,1,0,-1]

size = int(input())
idx = 0
while size :
    idx += 1
    cave = [list(map(int,input().split())) for _ in range(size)]

    distance = [[float("inf")] * size for _ in range(size)]

    q=[[cave[0][0],0,0]] # idx 0 : 거리, 1 : i, 2 : j
    distance[0][0] = cave[0][0]

    # 다익스트라 
    while q :
        dist_now, i,j = heappop(q)

        if distance[i][j] >= dist_now :
            for dt in range(4):
                di = i + dx[dt]
                dj = j + dy[dt]

                if 0 <= di < size and 0 <= dj < size :
                    cost = dist_now + cave[di][dj]

                    if cost < distance[di][dj]:
                        distance[di][dj] = cost
                        heappush(q,(cost,di,dj))
                        
    print(f"Problem {idx}: {distance[size-1][size-1]}")

    size = int(input())