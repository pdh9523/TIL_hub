def backtrack(idx=0, tmp=100):
    global ans
    if tmp <= ans :
        return
    
    elif idx == size:
        ans = tmp
        
    
    
    for i in range(size):
        if not visit[i] :
            visit[i] = 1
            backtrack(idx+1,tmp*arr[idx][i]/100)
            visit[i] = 0


for tc in range(int(input())):
    size = int(input())

    arr = [list(map(int,input().split())) for _ in range(size)]
    
    visit =[0] * size
    ans = 0
    backtrack()

    print(f"#{tc+1} {round(ans,6):.06f}")