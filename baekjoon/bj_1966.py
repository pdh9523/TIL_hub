# enumerate
from collections import deque
for _ in range(int(input())):
    N,M = map(int,input().split())
    printer = list(map(int,input().split()))
    q = deque(enumerate(printer))
    printer.sort(reverse=True)
    printer = deque(printer)
    cnt = 0 
    while True :
        if printer[0] == q[0][1] :
            printer.pop(0)
            a = q.popleft()
            cnt+=1
            if a[0] == M:
                break
        else :
            q.append(q.popleft())
    print(cnt)