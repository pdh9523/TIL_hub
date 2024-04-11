def backtrack(idx=0, ans=[]):
    if idx == M:
        print(*ans)
        return 
        
    for i in range(N):
        backtrack(idx+1, ans+[arr[i]])


N,M = map(int,input().split())
arr = sorted(list(map(int,input().split())))

backtrack()