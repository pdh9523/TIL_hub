from collections import deque

N,K = map(int,input().split())

q = deque([K])
visit = [0] * (K+1)

while q :
    s = q.popleft()
    
    if s % 2 == 1 :
        if visit[s+1] >= visit[s]+1 :
            visit[s+1] = visit[s]+1
            q.append(s+1)
    else :
        if visit[s-1] >= visit[s]+1:
            visit[s-1] = visit[s]+1
            q.append(s-1)
        if visit[s//2] >= visit[s]+1:
            visit[s//2] = visit[s]+1
            q.append(s//2)
    
    