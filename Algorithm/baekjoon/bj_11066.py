import sys; input = sys.stdin.readline


for _ in range(int(input())):
    N = int(input())
    arr = [*map(int,input().split())]

    DP = [[0]*N for _ in range(N)]

    for x in range(1,N):
        for i in range(N-x):

            j = i+x
            DP[i][j] = float('inf')

            tmp = sum(arr[i:j + 1])
            for k in range(i,j):
                DP[i][j] = min(DP[i][j], (DP[i][k] + DP[k+1][j] + tmp))
    print(DP[0][-1])
