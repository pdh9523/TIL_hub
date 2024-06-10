N,M = map(int,input().split())
arr = [ [*map(int,list(input()))] for _ in range(N) ]

size = min(N,M)

while size > 0: 
    for i in range(N):
        for j in range(M):
            if i+size < N and j+size <M:
                if arr[i][j] == arr[i+size][j] == arr[i][j+size] == arr[i+size][j+size]:
                    exit(print((size+1)**2))
            else : break
    size-=1
print(1)