from heapq import heappop, heappush

N,M,R = map(int,input().split())
arr = [*map(int,input().split())]
graph = [[] for _ in range(N)]
for _ in range(R):
    a,b,cost = map(int,input().split())
    graph[a].append((b,cost))
    graph[b].append((a,cost))

ans = 0 

for i in range(1,N+1):
    distance = [float('inf')]*(N+1)
    distance[i] = 0
    hq = [(0,i)]

    while hq :
        dist_now, now = heappop(hq)

        if dist_now > distance[now]:continue

        for next,cost in graph[now]:
            dist_next = dist_now+cost
            if distance[next] > dist_next:
                distance[next] = dist_next
                heappush(hq,(dist_next,next))
    
    tmp = 0 
    for idx,value in enumerate(arr):
        if M >= distance[idx]:
            tmp += value
    ans = max(ans,tmp)

print(ans)