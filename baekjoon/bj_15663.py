def backtrack(result = []) :
    if len(result) == M :
        result = list(map(lambda x : x[1], result))
        ans.add(tuple(result))
        return

    for i in arr :
        if i not in result :
            backtrack(result + [i])


N,M = map(int,input().split())

arr = list(enumerate(map(int,input().split())))
ans = set()
backtrack()

for answer in sorted(ans):
    print(*answer)