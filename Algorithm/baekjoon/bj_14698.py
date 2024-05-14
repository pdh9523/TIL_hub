import sys
from heapq import heappush, heappop, heapify

input = sys.stdin.readline


for _ in range(int(input())):
    N = int(input())
    arr = [*map(int,input().split())]
    heapify(arr)
    ans = 1
    while len(arr) > 1 :
        tmp = heappop(arr) * heappop(arr)
        ans *= tmp%1000000007
        heappush(arr,tmp)
    print(ans%1000000007)