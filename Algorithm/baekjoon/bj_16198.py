def backtrack(res=0):
    global ans

    if len(arr) == 2:
        ans = max(ans, res)

    for i in range(1, len(arr)-1):
        tmp = arr[i-1]*arr[i+1]
        l = arr.pop(i)
        backtrack(res+tmp)
        arr.insert(i,l)

N = int(input())
arr = [*map(int, input().split())]
ans = -float('inf')
backtrack()
print(ans)