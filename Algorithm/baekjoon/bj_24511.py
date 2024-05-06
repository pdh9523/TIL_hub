from collections import deque

N = int(input())
style = [*map(int,input().split())]
elements = [*map(int,input().split())]

M = int(input())
new_elem = [*map(int,input().split())]

q = deque()

for i in range(N):
    if style[i] == 0 :
        q.appendleft(elements[i])
q.extend(new_elem)
print(*list(q)[:M])