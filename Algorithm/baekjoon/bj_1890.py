N = int(input())

arr = [ [*map(int,input().split())] for _ in range(N) ]

DP = [ [0] * N for _ in range(N) ]

DP[0][0] = 1
for i in range(N):
    for j in range(N):
        tmp = arr[i][j]
        if tmp == 0 :
            continue
        if 0 <= i + tmp < N :
            DP[i+tmp][j] += DP[i][j]
        if 0 <= j + tmp < N : 
            DP[i][j+tmp] += DP[i][j]
print(DP[-1][-1])