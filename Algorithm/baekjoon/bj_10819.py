def backtrack(idx=0, visit=[], result=[]):
    global ans
    if idx == N:
        tmp=0
        for i in range(N-1):
            tmp += abs(result[i]-result[i+1])
        ans = max(ans,tmp)
        return 

    for i in range(N):
        if i not in visit :
            backtrack(idx+1, visit+[i], result+[arr[i]])

N = int(input())
arr = [ *map(int,input().split()) ]

ans = 0
backtrack()
print(ans)