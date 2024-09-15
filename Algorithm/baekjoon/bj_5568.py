def backtrack(visit, res=[], idx=0):
    if idx==K:
        tmp = "".join(res)
        data.add(tmp)
        return;
    
    for i in range(N):
        if not visit[i]:
            visit[i] = 1
            res.append(str(arr[i]))
            backtrack(visit, res, idx+1)
            res.pop()
            visit[i] = 0


N = int(input())
K = int(input())

data = set()
arr = [int(input()) for _ in range(N)]
visit = [0]*N
backtrack(visit)
print(len(data))