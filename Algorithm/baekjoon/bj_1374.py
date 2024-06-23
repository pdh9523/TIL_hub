import sys 
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input())
arr = sorted([ [*map(int,input().split()[1:])] for _ in range(N)])
hq, cnt = [],0

for i in arr:
    while hq and hq[0] <= i[0]:
        heappop(hq)
    heappush(hq,i[1])
    cnt = max(cnt,len(hq))
print(cnt)