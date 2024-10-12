N,M = map(int,input().split())
arr = [[0]*(M+1) for _ in range(N+1)]
data = dict()
for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    if a+b > c+d: a,b,c,d = c,d, a,b
    data[(c,d)] = data.setdefault((c,d), set()) | {(a,b)}

for i in range(N+1):
    if (i,0) in data and (i-1,0) in data[(i,0)]: break
    arr[i][0] = 1

for j in range(M+1):
    if (0,j) in data and (0,j-1) in data[(0,j)]: break
    arr[0][j] = 1


for i in range(1,N+1):
    for j in range(1,M+1):
        top = arr[i-1][j]
        left = arr[i][j-1]

        if (i,j) in data:
            if (i-1,j) in data[(i,j)]: top = 0
            if (i,j-1) in data[(i,j)]: left = 0

        arr[i][j] = top + left
print(arr[N][M])