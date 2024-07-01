N = int(input())
arr = [list(input()) for _ in range(N)]

visit = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        for k in range(N):
            if k==i: continue

            if not visit[i][k]:
                if arr[i][k]=="Y" : visit[i][k] = 1
                if arr[i][j]=="Y" and arr[j][k]=="Y": visit[i][k] = 1
print(max([*map(sum,visit)]))