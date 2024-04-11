def backtrack(result=[]):
    if len(result) == M:
        print(*result)
        return
    
    for i in arr:
        if i not in result:
            backtrack(result + [i])


N,M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()

backtrack()