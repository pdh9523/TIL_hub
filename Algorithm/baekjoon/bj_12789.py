from collections import deque

t = int(input())

tc = deque((range(1,t+1)))

line = list(map(int,input().split()))

stack = []

for man in line :
    if man == tc[0]:
        tc.popleft()

    else :
        stack.append(man)

    while stack and stack[-1] == tc[0]:
        stack.pop()
        tc.popleft()

if not tc and not stack :
    print("Nice")
else :
    print("Sad")