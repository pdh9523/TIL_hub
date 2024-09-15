import sys; input = sys.stdin.readline
from heapq import heappop, heappush


dr = (1,0),(0,1),(-1,0),(0,-1)

N = int(input())
arr = [[*map(int,input().split())] for _ in range(N)]
distance = [[float('inf')]*N for _ in range(N)]
distance[0][0] = 0
# dst, i,j
hq = [(0,0,0)]

while hq:
    dist_now,x,y = heappop(hq)

    if dist_now > distance[x][y]: continue

    for dx,dy in dr:
        di,dj = x+dx, y+dy      # next
        if 0<=di<N and 0<=dj<N:
            cost = max(dist_now, abs(arr[x][y] - arr[di][dj]))
            
            if distance[di][dj] > cost:
                distance[di][dj] = cost
                heappush(hq, (cost, di,dj))
print(distance[-1][-1])