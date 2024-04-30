def backtrack(idx=0):
    global ans
    
    if idx == N:
        total = 0
        for i in range(N):
            if egg[i][0] <= 0:
                total += 1

        ans = max(ans,total)
        return
    
    if egg[idx][0] <= 0:
        backtrack(idx+1)
        return


    for i in range(N):
        if i == idx : continue
        if egg[i][0] > 0 :
            break
    else :
        ans = max(ans,N-1) 
        return


    for i in range(N):
        if i == idx or egg[i][0] <= 0 : continue

        egg[idx][0] -= egg[i][1]
        egg[i][0] -= egg[idx][1]

        backtrack(idx+1)

        egg[idx][0] += egg[i][1]
        egg[i][0] += egg[idx][1]


N = int(input())
egg = [ [*map(int,input().split())] for _ in range(N) ] #내구도와 무게

ans = 0
backtrack()

print(ans)