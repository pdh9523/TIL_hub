import sys; input = sys.stdin.readline


def bellman_ford():
    distance = [-float('inf')]*N
    distance[S] = benefit[S]

    for i in range(N-1):
        for s,e,w in graph:
            if distance[s] != -float('inf') and distance[s] + w > distance[e]:
                distance[e] = distance[s] + w
                
    if distance[E] == -float('inf'):
        return "gg"
    
    for s,e,w in graph:
        if distance[s] != -float('inf') and distance[s] + w > distance[e]:
            if dfs(e):
                return "Gee"

    return distance[E]

def dfs(start):
    stack = [start]
    visit = [False]*N
    while stack:
        now = stack.pop()
        if now == E:
            return True
        
        if not visit[now]:
            visit[now] = True
            for s,e,c in graph:
                if s != now: continue
                stack.append(e)
    return False

N,S,E,M = map(int,input().split())

tmp = [[*map(int,input().split())] for _ in range(M)]
benefit = [*map(int,input().split())]
graph = [] 
for s,e,c in tmp:
    graph.append((s,e,benefit[e] - c))
print(bellman_ford())