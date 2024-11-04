import sys; input = sys.stdin.readline
from heapq import heappop, heappush


arr = sorted([[*map(int,input().split())] for _ in range(int(input()))])
hq = []
for d,c in arr:
    heappush(hq, c)
    if len(hq) > d: heappop(hq)
    
print(sum(hq))