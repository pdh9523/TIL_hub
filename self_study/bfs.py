def dfs(s,N) :  #  s: start N : node
    q = []
    visited = [0] * (N+1)

    q.append(s)
    while q :
        t = q.pop(0)
        if t == G :
            return visited[t]
        for i in adjl[t] :
            if visited[i]==0 :
                q.append(i)
                visited[i] = visited[t]+1
    return 0

G = 1 # 목표지점
t = int(input())

adjl = [tuple(map(int, input().split()) for _ in range(t))] # 인접 리스트
