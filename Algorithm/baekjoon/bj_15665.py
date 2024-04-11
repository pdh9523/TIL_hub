def backtrack(idx=0, result=[]):
    if idx == M :
        ans.append(result)
        return
    
    for i in range(N):
        backtrack(idx+1, result+[arr[i]])

N,M = map(int,input().split())
arr = sorted(list(set(map(int,input().split()))))
N = len(arr)
ans = []
backtrack()

for answer in sorted(ans) :
    print(*answer)