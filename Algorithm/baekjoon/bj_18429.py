def backtrack(idx=0,weight=0,visit=[]):
    global ans
    if idx == N:
        if weight >=0:
            ans += 1
        return
    
    for i in range(N) :
        if weight + arr[i] - K >= 0 and i not in visit:
            backtrack(idx+1,weight+arr[i]-K, visit+[i])

N,K = map(int,input().split())

arr = [*map(int,input().split())]
ans = 0
backtrack()
print(ans)