def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else :
        parent[a] = b

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

N,M = map(int,input().split())

parent = list(range(N+1))

graphs = []
for _ in range(M):
    a,b,cost = map(int,input().split())
    graphs.append((cost,a,b))

graphs.sort()

ans = 0
for graph in graphs :
    cost, a, b = graph

    if find(parent,a) != find(parent,b):
        union(parent,a,b)
        ans += cost

print(ans)