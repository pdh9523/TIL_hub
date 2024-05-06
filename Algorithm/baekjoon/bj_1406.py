import sys
from collections import deque

input = sys.stdin.readline


left,right = deque(input().strip()),deque()
# 커서는 left와 right 사이에 있음
for _ in range(int(input())):
    order,*char = input().split()

    if order == "L":    
        if left :
            right.appendleft(left.pop())
    
    elif order == "D":
        if right :
            left.append(right.popleft())
    
    elif order == "B":
        if left :
            left.pop()
            
    elif order == "P":
        left.append(*char)

print(*(left+right), sep="")