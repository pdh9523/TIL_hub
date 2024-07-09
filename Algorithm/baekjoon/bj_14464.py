import sys
from heapq import heappush, heappop

input = sys.stdin.readline


N,M = map(int,input().split())
stocks = [(int(input()),) for _ in range(N)] + [tuple(map(int, input().split())) for _ in range(M)]
stocks.sort(key=lambda x: (x[0], -len(x)))

hq = []
ans = 0
for stock in stocks:
    if len(stock) == 2:
        heappush(hq, stock[1])
    else:
        while hq and hq[0] < stock[0]:
            heappop(hq)
        if hq:
            heappop(hq)
            ans += 1
print(ans)

