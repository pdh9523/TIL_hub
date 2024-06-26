from collections import deque

def check(a,b,c):
    if not visit.get((a,b)):
        visit[(a,b)]=1
        q.append((a,b,c+1))

S = int(input())
q = deque([(1,0,0)])

visit = dict()
while q:
    window, clipboard,cnt = q.popleft()
    
    if window == S : print(cnt) ; break
    
    check(window, window, cnt+1)
    check(window+clipboard, clipboard, cnt+1)
    check(window-1, clipboard, cnt+1)