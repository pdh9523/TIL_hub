from collections import deque

dr = (1,0),(0,1),(-1,0),(0,-1)

def backtrack(i=0,j=-1,visit=[]):
    if len(visit)==5:
        if dfs(visit):
            tmp = 0
            for dx,dy in visit:
                tmp += arr[dx][dy]
            data[tuple(sorted(visit))] = tmp
    j += 1
    if j == M:
        i += 1
        j = 0
    if i == N:
        return
    backtrack(i,j,visit+[(i,j)])
    backtrack(i,j,visit)


def dfs(arr):
    visit = [[0]*M for _ in range(N)]

    for i,j in arr:
        visit[i][j] = 1
    q = deque([(i,j)])
    while q:
        x,y = q.popleft()

        for dx,dy in dr:
            di,dj = x+dx, y+dy
            if 0 <=di<N and 0<=dj<M:
                if visit[di][dj]:
                    visit[di][dj] = 0
                    q.append((di,dj))
    if any(map(sum, visit)):
        return False
    return True



N,M = map(int,input().split())
arr = [[*map(int,input().split())] for _ in range(N)]

data = dict()
backtrack()


ans = -float('inf')
# 오답인듯
# ans = 0
for i in data:
    for j in data:
        if len(set(i) & set(j)) == 2:
            ans = max(ans, data[i] + data[j])
print(ans)