import sys
from collections import deque

input = sys.stdin.readline
t = int(input())

q = deque()
for _ in range(t):
    order = input().split()
    

    if order[0] == "push_back":
        q.append(order[1])
    elif order[0] == "push_front":
        q.appendleft(order[1])
    elif order[0] == "front":
        if len(q) > 0 :
            print(q[0])
        else : 
            print(-1)
    elif order[0] == "back":
        if len(q) > 0 :
            print(q[-1])
        else :
            print(-1)
    elif order[0] == "size":
        print(len(q))
    elif order[0] == "empty":
        if len(q) == 0 :
            print(1)
        else :
            print(0)
    elif order[0] == "pop_front":
        if len(q) > 0 :
            print(q.popleft())
        else :
            print(-1)
    elif order[0] == "pop_back":
        if len(q) > 0 :
            print(q.pop())
        else :
            print(-1)