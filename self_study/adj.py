
def DFS(start) :
    stack = [start]
    while stack :
        now = stack.pop()
        if visited[now] == 0 :
            visited[now] = 1
            print(now, end=" ")
            for next in adj[now] :
                if visited[next] == 0 :
                    stack.append(next)



# 1로 표현한 곳이 갈 수 있다는 뜻 adj[출발][도착]
for idx in range(E) :
    adj[arr[idx*2]][arr[idx*2+1]] = 1
    adj[arr[idx*2+1]][arr[idx*2]] = 1   # 양쪽으로 돌 수 있으면 촌수 계산할 수 있는 거 아님? 캬~

# 인접 행렬
    
def DFS(start) :
    stack = [start]
    while stack :
        now = stack.pop()
        if visited[now] == 0 :
            visited[now] = 1
            print(now, end=" ")
            for next in range(1,V + 1) :
                # adj[now == 1][next == 1~7]
                if visited[next] == 0 and adj[now][next] == 1 :
                    stack.append(next)

# 재귀
                    
def DFS(start) :
    visited[start] = 1
    print(start. end=" ")
    for next in range(1,V+1) :
        if visited[next] == 0 and adj[start][next] == 1:
            DFS(next)