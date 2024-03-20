from collections import deque

for idx in range(int(input())):

    N,M = map(int,input().split())

    visit = [0] * 1000001

    q = deque([M])
    visit[M] = 0

    while q : 
        s = q.popleft()
        
        if s == N:    
            print(f"#{idx+1} {visit[s]}")
            break

        if s % 2 == 0 :                             # 2로 나뉘어 지는 경우 
            if visit[s//2] == 0 :                   
                q.append(s//2)
                visit[s//2] = visit[s]+1            

        if s+10 <= 1000000 and visit[s+10] == 0 :   # 10을 빼는 경우

            visit[s+10] = visit[s]+1
            q.append(s+10)

        if s-1>0 and visit[s-1] == 0:               # 1을 더하는 경우
            visit[s-1] = visit[s]+1
            q.append(s-1)

        if s+1 <= 1000000 and visit[s+1] == 0:      # 1을 빼는 경우
            visit[s+1] = visit[s]+1
            q.append(s+1)
