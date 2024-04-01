for _ in range(int(input())):
    N,M,W = map(int,input().split())

    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        s,e,t = map(int,input().split())
        graph[s].append((e,t))
        graph[e].append((s,t))
    
    for _ in range(W):
        s,e,t = map(int,input().split())
        graph[s].append((e,-t))

    distance = [0] * (N+1)
    check = False
    for i in range(N):
        for now in range(1, N+1):
            for next, dist_next in graph[now]:
                if distance[next] > distance[now] + dist_next :
                    distance[next] = distance[now] + dist_next
                    if i == N-1:
                        print("YES")
                        check = True
                        break
            if check:
                break
        if check:
            break

    else :
        print("NO")
        