from heapq import heappush, heappop
import sys


input = sys.stdin.readline

N,H,T = map(int,input().split())

hq = [ ]
for _ in range(N):
    heappush(hq, -int(input()))

check = True
for i in range(T+1):
    
    if check and -hq[0] < H :
        print("YES")
        print(i)
        check = False
    
    if check and i == T:
        print("NO")
        print(-hq[0])
        break
    
    target = -heappop(hq)

    if target != 1 :
        target //=2
    
    heappush(hq,-target)