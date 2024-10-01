import sys; input = sys.stdin.readline
from collections import deque

def compare(a,b):
    cnt =0 
    for i,j in zip(a,b):
        if i==j:
            cnt += 1
    return cnt==3

def make_prime():
    for i in range(2,10000):
        for j in sorted(prime):
            if i%j == 0: break
        else:
            prime.add(i)
            if i>1000:
                data.add(i)


prime = set()
data = set()
make_prime()
for _ in range(int(input())):
    a,b = map(int,input().split())
    visit = dict()
    q = deque([a])
    visit[a] = 0
    while q:
        now = q.popleft()

        if now == b:
            print(visit[now])
            break

        for nxt in data:
            if nxt in visit: continue
            if not compare(str(nxt), str(now)): continue

            visit[nxt] = visit[now]+1
            q.append(nxt)
    