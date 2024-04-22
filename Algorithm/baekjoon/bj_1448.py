import sys
from heapq import heappop, heappush


input = sys.stdin.readline

N = int(input())
hq = []

for _ in range(N):
    heappush(hq,-int(input()))

c = -heappop(hq)
b = -heappop(hq)
a = -heappop(hq)

while c >= a+b :
    b,c = a,b
    
    if not hq :
        exit(print(-1))
    a = -heappop(hq)

print(a+b+c)