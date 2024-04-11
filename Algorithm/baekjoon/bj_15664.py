def backtrack(idx=0, result=[], visit=[]):
    if idx == M :
        result.sort()
        if result not in ans :
            ans.append(result)
        return

    for i in range(N):
        if i not in visit :
            backtrack(idx+1, result+[arr[i]], visit+[i])

N,M = map(int,input().split())

arr = sorted(list(map(int,input().split())))
ans = []
backtrack()
for answer in ans :
    print(*sorted(answer))