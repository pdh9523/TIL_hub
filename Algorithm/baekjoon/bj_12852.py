from collections import deque


N = int(input())
q = deque([[N]])
visit = dict()
while q:
    now = q.popleft()
    a = now[-1]

    if a == 1:
        break

    if a % 3 == 0:
        if a//3 not in visit or visit[a//3] > len(now):
            q.append(now+[a//3])
    if a % 2 == 0:
        if a//3 not in visit or visit[a//2] > len(now):
            q.append(now+[a//2])
    if a-1 not in visit or visit[a-1] > len(now):
        q.append(now+[a-1])

print(len(now)-1)
print(*now)