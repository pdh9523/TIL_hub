import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    command = deque(input().strip().replace("RR", ""))
    size = int(input())
    arr = deque(eval(input().strip()))
    rot = 0
    while command :
        s = command.popleft()

        if s == "D":
            if not arr :
                print("error")
                break
            else :
                if rot == 0 :
                    arr.popleft()
                else :
                    arr.pop()
        else :
            rot = 1 - rot

    else:
        if rot == 1 :
            arr.reverse()
        arr = list(map(str,arr))
        print("["+",".join(arr)+"]")
