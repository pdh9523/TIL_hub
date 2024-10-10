import sys; input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque([(0,0,0)])
    ans = 1
    time = True
    while q:
        for _ in range(len(q)):
            x, y, cnt = q.popleft()
            
            if x == N-1 and y == M-1: return ans
            
            for dy, dx in dr:
                di, dj = x + dy, y + dx
                if di < 0 or di >= N or dj < 0 or dj >= M or visit[di][dj] <= cnt:
                    continue
                if arr[di][dj] == '0':
                        q.append((di, dj, cnt))
                        visit[di][dj] = cnt

                elif cnt < K:
                    if not time:
                        q.append((x, y, cnt))
                    else:
                        visit[di][dj] = cnt
                        q.append((di, dj, cnt + 1))
        ans += 1
        time = not time
    return -1


dr = (1,0), (-1,0), (0,1), (0,-1)

N,M,K = map(int, input().split())
arr = [input().strip() for _ in range(N)]
visit = [[K+1 for _ in range(M)] for _ in range(N)]
visit[0][0] = 0


print(bfs())