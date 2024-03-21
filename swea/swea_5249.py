from heapq import heappush, heappop

for idx in range(int(input())):

    N,M = map(int,input().split())

    graph = [[] for _ in range(N+1)]

    for _ in range(M):                      # 양방향 그래프 제작
        a,b,l = map(int,input().split())
        graph[a].append((l,b))
        graph[b].append((l,a))
    
    # 프림 알고리즘
    hq = [(0,0)]
    
    visit = [False] * (N+1)                 
    ans = 0
    while hq :
        dist_now, now = heappop(hq)

        if not visit[now] :
            visit[now] = True
            ans += dist_now

            for item in graph[now]:
                heappush(hq,item)
                
    print(f"#{idx+1} {ans}")