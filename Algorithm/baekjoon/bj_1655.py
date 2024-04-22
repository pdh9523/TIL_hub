import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input())

left, right = [], []
# 왼 : 최대, 오 : 최소
for i in range(N):
    num = int(input())

    if len(left) == 0 or -left[0] >= num :
        heappush(left, -num)
    else : 
        heappush(right, num)

    if len(right) > len(left):
        temp = heappop(right)
        heappush(left, -temp)
    elif len(left) > len(right)+1 :
        temp = heappop(left)
        heappush(right, -temp)

    print(-left[0])