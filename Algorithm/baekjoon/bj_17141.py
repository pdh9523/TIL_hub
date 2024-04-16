from itertools import combinations
from collections import deque


dr = ((1,0),(0,1),(-1,0),(0,-1))

N, M = map(int,input().split())

lab = [list(map(int,input().split())) for _ in range(N)]

viruses = []

for i in range(N):
    for j in range(N):
        if lab[i][j] == 2 :
            viruses.append((i,j))

ans = float('inf')
for virus in list(combinations(viruses,M)):

    q = deque(virus)

    visit = [ [-1] * N for _ in range(N) ]

    copied = [row[:] for row in lab]
    for i,j in virus :
        visit[i][j] = 0
        copied[i][j] = 3

    tmp = 0

    while q :
        i,j = q.popleft()

        for dx, dy in dr :
            di, dj = i+dx, j+dy
            if 0 <= di < N and 0 <= dj < N :
                if  copied[di][dj] != 1 and visit[di][dj] == -1 and copied[di][dj] != 3:
                    visit[di][dj] = visit[i][j] + 1
                    copied[di][dj] = 3
                    q.append((di,dj))
                    tmp = max(tmp,visit[di][dj])

    for i in range(N):
        if 2 in copied[i] or 0 in copied[i] :
            break
    else :
        ans = min(ans,tmp)

print(ans if ans != float('inf') else -1)