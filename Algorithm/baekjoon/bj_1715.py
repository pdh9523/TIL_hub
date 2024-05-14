import sys
from heapq import heappush, heappop, heapify

input = sys.stdin.readline


hq = [int(input()) for _ in range(int(input()))]
heapify(hq)
ans = 0 
while len(hq) > 1 :
    tmp = heappop(hq) + heappop(hq)
    ans += tmp
    heappush(hq, tmp)

print(ans)