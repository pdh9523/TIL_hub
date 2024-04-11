# D : (2 * n) % 10000
# S : (n - 1) % 10000
# L : 1234 -> 2341
# R : 1234 -> 4123
from collections import deque

for _ in range(int(input())):
    A,B = map(int,input().split())
    visit = [0] * 10001
    q = deque([[A,""]])
    visit[int(A)] = True


    while q :
        now, code = q.popleft()

        if now == B :
            print(code)
            break
        
        # D
        d = 2*now % 10000
        if not visit[d]:
            visit[d] = 1
            q.append([d, code+"D"])
        
        # S
        s = (now-1) % 10000
        if not visit[s]:
            visit[s] = 1
            q.append([s, code+"S"])
        
        # L 
        l = now % 1000 * 10 + now//1000
        if not visit[l]:
            visit[l] = 1
            q.append([l,code+"L"])
        
        # R
        r = now // 10 + now % 10 * 1000
        if not visit[r] :
            visit[r] = 1
            q.append([r,code+"R"])

        