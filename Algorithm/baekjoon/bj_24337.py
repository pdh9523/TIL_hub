from collections import deque

N,A,B = map(int,input().split())
res = deque()
if A>=B: 
    check = 1
else: 
    A,B = B,A
    check = 0
for a in range(1,A+1):
    res.append(a)

for b in range(B-1,0,-1):
    res.append(b)
if N < len(res):
    exit(print(-1))

if check :
    while N > len(res):
        res.appendleft(1)
else:
    res.reverse()
    while N > len(res):
        res.insert(1,1)
print(*res)