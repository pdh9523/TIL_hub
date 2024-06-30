from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(10**5)


def DFS(now, dist_now=0):
    for next,cost in tree[now]:
        dist_next = dist_now+cost
        if visit[next]<0:
            visit[next]=dist_next
            DFS(next,dist_next)

N = int(input())
tree = [ [] for _ in range(N+1) ]

for _ in range(N-1):
    a,b,dist = map(int,input().split())
    tree[a].append((b,dist))
    tree[b].append((a,dist))

visit = [-1]*(N+1)
visit[1] = 0
DFS(1)
idx = 0 
for i in range(1,N+1):
    if visit[i] > visit[idx]: idx = i

visit = [-1]*(N+1)
visit[idx]=0
DFS(idx)

print(max(visit))