def backtrack(idx=0,result=[]) :
    if len(result) == 6 :
        print(*result)
        return
    if idx < N :
        backtrack(idx+1,result+[arr[idx]])
        backtrack(idx+1,result)

while True :
    N,*arr= map(int,input().split())
    if N == 0 :
        exit()
    backtrack()
    print()