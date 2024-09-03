from collections import deque


def add_q(now, nxt):
    if 0 <= nxt <= 100000:
        if nxt in visit: return
        visit[nxt] = visit[now] + 1
        q.append(nxt)


A,B,N,M = map(int,input().split())

q = deque([N])
visit = dict()
visit[N] = 0

while q:
    now = q.popleft()

    if now == M:
        exit(print(visit[now]))

    for w in A,B:
        nxt = now * w
        add_q(now, nxt)

    for w in -A,A,-B,B,-1,1:
        nxt = now + w
        add_q(now, nxt)
