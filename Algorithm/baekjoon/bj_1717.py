import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


N,M = map(int,input().split())
parent = list(range(N+1))

def find(x):
    if parent[x] != x :
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b :
        parent[b]=a
    else :
        parent[a]=b

for _ in range(M):
    order,a,b = map(int,input().split())

    if order == 0 :
        union(a,b)
    else: 
        print("YES" if find(a) == find(b) else "NO")


# DFS 13%에서 멈춤

# def dfs(start,end):
#     stack = [start]
#     visit = dict()
#     while stack :
#         now = stack.pop()
        
#         if now == end :
#             return True
        
#         if not visit.get(now):

#             visit[now]=1

#             if graph.get(now):
#                 stack.extend(graph[now])
#     return False


# N,M = map(int,input().split())
# graph = dict()

# for _ in range(M): 
#     order,a,b = map(int,input().split())

#     if order == 0 :
#         graph[a] = graph.get(a,[]) + [b]
#         graph[b] = graph.get(b,[]) + [a]

#     else: 
#         print("YES" if dfs(a,b) else "NO")
