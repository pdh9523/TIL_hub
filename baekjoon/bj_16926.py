from copy import deepcopy

dx = [1,0,-1,0]
dy = [0,1,0,-1]


def rotate(lst) :
    tmp = deepcopy(lst)
    dr = 0
    i,j = 0,0
    for i in range(4):
        while True: 
            di = i + dx[dr]
            dj = j + dy[dr]
            if not (0<= di < N and 0 <= dj < M) :
                break
            lst[i][j] = tmp[di][dj]
            i,j=di,dj
        dr += 1

N,M,R = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
rotate(arr)

print(arr)