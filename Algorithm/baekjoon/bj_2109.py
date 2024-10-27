import sys; input = sys.stdin.readline
from heapq import heappop, heappush

hq = []
for _ in range(int(input())):
    a,b = map(int,input().split())
    heappush(hq, (-a, b))

ans = [0] * 21
while hq:
    a, b = heappop(hq)
    for i in range(b,0,-1):
        if not ans[i]:
            ans[i] = -a
            break
print(sum(ans))

### 
import sys; input = sys.stdin.readline
from heapq import heappop, heappush


N = int(input())
arr = sorted([[*map(int,input().split())] for _ in range(N)], key=lambda x: x[1])
hq = []
for p,d in arr:
    heappush(hq, p)
    if len(hq) > d: heappop(hq)
    
print(sum(hq))