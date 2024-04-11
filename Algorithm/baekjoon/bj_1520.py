from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

N,M = map(int,input().split())
load = list(map(int,input().split()) for _ in range(N))


q = deque([(0,0)])
visit = [[0]*M for _ in range(N)]
while q :
    i,j = q.popleft()
    