def backtrack(result=[]):
    if len(result) == M:
        print(*result)
        return
    else :
        for i in range(1,N+1):
            if i not in result :
                if not result or result[-1] < i :
                    backtrack(result+[i])
            
N,M = map(int,input().split())

backtrack()