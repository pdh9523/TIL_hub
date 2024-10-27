def backtrack(idx, res=""):
    if idx == 0:
        return ans.append(res)

    for i in range(10):
        i = str(i)
        if not res or res[-1] > i:
            backtrack(idx-1, res+i)

N = int(input())
ans = []
for i in range(1,11):
    backtrack(i)
print(ans[N] if N < len(ans) else -1)