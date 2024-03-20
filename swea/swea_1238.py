from collections import deque
for idx in range(1,11):  
    size, start = map(int,input().split())

    data = list(map(int,input().split()))

    graph = [[] for _ in range(101)]

    for i in range(0,size,2):
        a,b=data[i],data[i+1]
        graph[a].append(b)

    q = deque([start])
    visit = [0] * 101
    visit[start] = 1
    while q :
        now = q.popleft()

        for item in graph[now]:
            if not visit[item]:
                visit[item] = visit[now]+1
                q.append(item)
    
    target = max(visit) 
    ans = []
    for ind in range(101):
        if visit[ind] == target :
            ans.append(ind)
    print(f"#{idx} {max(ans)}")