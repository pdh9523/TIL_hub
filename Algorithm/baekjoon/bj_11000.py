import sys
from heapq import *

input = sys.stdin.readline

q = []
N = int(input())
arr = sorted([list(map(int,input().split())) for _ in range(N)])

heappush(q, arr[0][1])  #첫번째 강의가 끝나는 시간을 넣음

for i in range(1, N):

    if q[0] > arr[i][0]:            # q[0] 강의실의 마치는 시간 (최소) > 새로 넣을 강의의 시작 시간
        heappush(q, arr[i][1])      # 새 강의실 만들기

    else:                           # 새로 넣을 강의를 제일 빨리 끝나는 강의실에 넣을 수 있다면
        heappop(q)                  # 그 강의실 빼고
        heappush(q, arr[i][1])      # 새로 넣기 (마지막)

print(len(q))