import sys; input=sys.stdin.readline

def multiply(arr,brr):
    res = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                res[i][j] += arr[i][k]*brr[k][j]
            res[i][j] %= 1000
    return res


def div_conq(arr,M):
    if M == 1:
        return arr
    
    tmp = div_conq(arr, M//2)

    if M%2:
        return multiply(multiply(tmp,tmp), arr)
    else:
       return multiply(tmp,tmp)


N,M = map(int,input().split())
arr = [[*map(int,input().split())] for _ in range(N)]

for ans in div_conq(arr,M): print(*ans)