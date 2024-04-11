def backtrack(idx=0, result=[]):

    if idx == M :
        print(*result)
        return
    
    for i in range(N):
        backtrack(idx+1, result + [arr[i]])


N,M = map(int,input().split())
arr = list(range(1,N+1))

backtrack()