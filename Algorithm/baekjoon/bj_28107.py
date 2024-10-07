import sys; input=sys.stdin.readline
from heapq import heappop, heappush


N,M = map(int,input().split())

data = dict()

for i in range(N):
    for num in [*map(int,input().split())][1:]:
        heappush(data.setdefault(num,list()), i)

ans = [0]*N
for k in map(int,input().split()):
    if k not in data: continue
    if not data[k]: continue
    ans[heappop(data[k])] += 1

print(*ans)