import sys
input = sys.stdin.readline

N,M = map(int,input().split())
teacher = set(tuple(map(int,input().split())) for _ in range(M))

visit = set()
q = [(0,0,0)]

while q:
    x,y,h = q.pop()

    if (x,y) == (N*2,0):
        exit(print(h))

    for dx,dy in (x+1, y-1), (x+1,y+1):
        if 0<=dy and dx+dy <= 2*N and (dx,dy) not in teacher and (dx,dy) not in visit:
            q.append((dx,dy,max(h,dy)))
            visit.add((dx,dy))

print(-1)
