def backtrack(idx=0, visit=[]):
    if idx == N :
        print(*visit)
        return
    for i in arr : 
        if i not in visit :
            backtrack(idx+1, visit+[i])

N = int(input())
arr = list(range(1,N+1))

backtrack()