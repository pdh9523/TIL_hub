from collections import deque


N = int(input())
arr = [*map(int,input().split())]
now = int(input())-1
q = deque([now])
visit = [0]*N
visit[now] = 1
while q:
    now = q.popleft()

    for i in -arr[now],arr[now]:
        if 0<= now+i < N: 
            if visit[now+i]: continue
            visit[now+i] = 1
            q.append(now+i)

print(sum(visit))