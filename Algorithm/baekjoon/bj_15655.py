def backtrack(idx=0, tmp=[], visit=[]):
    if idx == M:
        tmp.sort()
        if tmp not in result :
            result.append(tmp)
            return
    for i in range(N):
        if i not in visit :
            backtrack(idx+1, tmp+[arr[i]], visit+[i])


N,M = map(int,input().split())
arr = sorted(list(map(int,input().split())))
result = []

backtrack()

for ans in result :
    print(*ans)
