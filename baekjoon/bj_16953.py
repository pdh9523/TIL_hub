from collections import deque 

A,B = map(int,input().split())


q = deque([A])
visit = {A:1}
while q:
    s = q.popleft()

    if s == B :
        exit(print(visit[s]))


    for i in (s*2, s*10+1):
        if i not in visit and s <= B:
            visit[i] = visit[s] +1
            q.append(i)
print(-1)