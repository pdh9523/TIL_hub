def backtrack(idx=0,visit=[]):
    if idx==length:
        ans.append("".join(list(map(lambda x : N[x], visit))))
        return
    for i in range(length):
        if i not in visit:
            backtrack(idx+1, visit+[i])

N = input()
length = len(N)

ans = [] 
backtrack()
ans.sort()
print(ans[ans.index(N)+1])