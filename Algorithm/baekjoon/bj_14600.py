N = int(input())
arr = [[0]*2*N for _ in range(2*N)]
i,j = map(int,input().split())
i,j = 2*N-j, i-1
arr[i][j] = -1