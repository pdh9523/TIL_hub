# W B R 순서대로


for t in range(int(input())):
    N,M = map(int,input().split())
    flag = [list(input()) for _ in range(N)]

    min_value = N*M

    flag_case = []
    
    for i in range(1, N-1):
        for j in range(i+1, N):
            flag_case.append([i,j])
    
    for idx,jdx in flag_case:
        cnt = 0
        for i in range(idx):           
            cnt += M - flag[i].count("W")
        for j in range(idx,jdx):
            cnt += M - flag[j].count("B")
        for k in range(jdx,N):
            cnt += M - flag[k].count("R")
        
        if min_value > cnt:
            min_value = cnt
    print(f"#{t+1} {min_value}")