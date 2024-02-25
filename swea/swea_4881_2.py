def backtrack(idx = 0, sums=0):
    global min_value

    if idx == size :

        if min_value > sums :
            min_value = sums
    
    elif sums >= min_value:
        return
    
    else :
        for i in range(idx,size):
            a,b = visit[i],visit[idx]
            a,b = b,a
            backtrack(idx+1, sums+test_list[idx][visit[idx]])
            a,b= b,a
            
t = int(input())

for i in range(t):    
    size = int(input())
    test_list = [list(map(int,input().split())) for _ in range(size)]
    visit = list(range(size))
    min_value = float("inf")

    backtrack()
    print(f"#{i+1} {min_value}")