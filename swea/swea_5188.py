from collections import deque
#BFS로 visit에 비용 저장

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for t in range(int(input())):
    size = int(input())
    arr = [list(map(int,input().split())) for _ in range(size)]

    cost = [[0]*size for _ in range(size)]
    # 튜플 방식으로 저장해 BFS 탐색
    q = deque([(0,0)])
    cost[0][0] = arr[0][0]
    while q :
        i,j = q.popleft()
        
        if (i,j) == (size-1,size-1):
            pass
    
        else :
            for dt in range(4) :
                di = i + dx[dt]
                dj = j + dy[dt]
                if 0<= di < size and 0 <= dj < size:
                    if cost[di][dj] == 0 or cost[di][dj] > cost[i][j]+arr[di][dj]:
                        q.append((di,dj))
                        cost[di][dj] = cost[i][j]+arr[di][dj]
    print(f"#{t+1} {cost[size-1][size-1]}")