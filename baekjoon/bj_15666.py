def backtrack(result = []):
    if len(result) == M:
        ans.add(tuple(result))
        return
    
    for i in arr :
        if not result or result[-1] <= i :
            backtrack(result+[i])


N,M = map(int,input().split())

arr = list(map(int,input().split()))
arr.sort()
ans = set()


backtrack()

for answer in sorted(ans):
    print(*answer)