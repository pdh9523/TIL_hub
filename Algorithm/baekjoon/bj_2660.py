import sys

input = sys.stdin.readline

N = int(input())

distance = [[float('inf')]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    distance[i][i] = 0

while True :
    a,b=map(int,input().split())
    if a == -1:
        break
    distance[a][b] = 1
    distance[b][a] = 1

for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            distance[i][k] = min(distance[i][k],distance[i][j]+distance[j][k])
            distance[k][i] = min(distance[k][i],distance[k][j]+distance[j][i])

ans = []
for dist in distance:
    ans.append(max(dist[1:]))

target = min(ans)
cand = []
for i in range(1,N+1):
    if ans[i] == target:
        cand.append(i)

print(target, len(cand))
print(*cand)