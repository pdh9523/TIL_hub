import sys; input = lambda: sys.stdin.readline().strip()
from heapq import heappop, heappush


N,M = map(int,input().split())
arr = [[*map(int, list(input()))] for _ in range(N)]

distance = [[float('inf')]*(M+1) for _ in range(N)]
distance[0][0] = 0

hq = [(0,0,0)]
while hq:
    now, dist_now, cnt = heappop(hq)

    if dist_now > distance[now][cnt]: continue

    for nxt in range(N):
        if nxt == now: continue
        dist_next = dist_now + arr[now][nxt]
        if distance[nxt][cnt] > dist_next:
            distance[nxt][cnt] = dist_next
            heappush(hq, (nxt, dist_next, cnt))
        
        if cnt < M:
            dist_next = dist_now + arr[now][nxt]/2
            if distance[nxt][cnt+1] > dist_next:
                distance[nxt][cnt+1] = dist_next
                heappush(hq, (nxt, dist_next, cnt+1))

print(min(distance[1]))