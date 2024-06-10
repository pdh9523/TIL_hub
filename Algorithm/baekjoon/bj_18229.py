N,M,K = map(int,input().split())
arr = [[*map(int,input().split())] for _ in range(N)]
ans = [0]*N

for j in range(M):
    for i in range(N):
        ans[i] += arr[i][j]

        if ans[i] >= K :
            exit(print(i+1,j+1))
