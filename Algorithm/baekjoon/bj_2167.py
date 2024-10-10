def sol(x1,y1, x2,y2):
    res = arr[x2][y2]
    if x1:
        res -= arr[x1-1][y2]
    if y1:
        res -= arr[x2][y1-1]
    if x1 and y1:
        res += arr[x1-1][y1-1]
    return res


N,M = map(int,input().split())
arr = [[*map(int,input().split())] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if i: arr[i][j] += arr[i-1][j]
        if j: arr[i][j] += arr[i][j-1]
        if i and j: arr[i][j] -= arr[i-1][j-1]

for _ in range(int(input())):
    x1,y1, x2,y2 = map(lambda x: int(x)-1,input().split())
    print(sol(x1,y1, x2,y2))