from collections import deque


N,M = map(int,input().split())
q = deque(range(1,N+1))
target = [*map(int,input().split())]
cnt = 0

for i in target :
    while q[0] != i :
        if q.index(i) <= len(q)//2:
            rot=-1
        else :
            rot=1
        q.rotate(rot)
        cnt += 1
    q.popleft()
print(cnt)