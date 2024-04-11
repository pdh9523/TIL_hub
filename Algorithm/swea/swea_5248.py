for idx in range(int(input())):

    N,M = map(int,input().split())
    tmp = list(map(int,input().split()))
    graph = [[] for _ in range(N+1)]
    
    for i in range(0,2*M,2):
        a,b = tmp[i], tmp[i+1]
        graph[a].append(b)
        graph[b].append(a)

    visit = [0] * (N+1)                         # 방문 확인 리스트
    cnt = 0
    
    for i in range(1,N+1):                      # 전체 인원을 순회하면서
    
        if not visit[i]:                        # 방문하지 않았다면

            stack = [i]                         # DFS 시행
            while stack :                       # stack이 빌 때까지
                s = stack.pop()                 # stack에서 하나씩 빼면서 확인
                visit[s] = 1                    # visit에 확인표시

                for item in graph[s]:           # 현재 확인 중인 곳에서 갈 수 있는 곳을 찾고
                    if not visit[item]:         # 거기가 아직 안간 곳이면
                        stack.append(item)      # stack에 더하기

            cnt+= 1                             # while문이 시행됐고, 끝났다면 cnt += 1
    print(f"#{idx+1} {cnt}")