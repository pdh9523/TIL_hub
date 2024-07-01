from sys import stdin
input = stdin.readline

def DFS(now, dist_now=0):    
    for next,cost in tree[now]:
        if visit[next]<0:
            dist_next = dist_now + cost
            visit[next] = dist_next
            DFS(next,dist_next)


N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N):
    data = [*map(int,input().split())]
    i=1
    idx = data[0]
    while True:
        if data[i] == -1: break
        jdx,dist=data[i],data[i+1] 
        tree[jdx].append((idx,dist))
        tree[idx].append((jdx,dist))
        i += 2

visit = [-1] * (N+1)
visit[1] = 0
DFS(1)
idx = 0
for i in range(N+1):
    if visit[i] > visit[idx]:idx=i

visit = [-1] * (N+1)
visit[idx] = 0
DFS(idx)

print(max(visit))