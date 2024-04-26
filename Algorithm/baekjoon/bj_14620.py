dr = (1,0),(0,1),(-1,0),(0,-1)

def backtrack(i=1,j=1,cnt=3,value=0):               # 백트래킹
    global ans
    tmp = value                                     # 원위치 할때 원래 값을 임시 변수에 저장

    if cnt == 0 :                                   # 꽃 3개를 다 심었다 ?
        ans = min(value, ans)                       # 비교하고 끝내기
        return
    
    if i == N-2 and j == N-1:                       # 끝까지 달렸다
        return                                      # 끝내기
    
    if j == N-1 :                                   # j가 범위를 벗어나려한다.
        i += 1                                      # 인덱스 조정
        j = 1

    
    if not visit[i][j]:                             # 현재 위치를 방문하지 않았다면,
        for dx,dy in dr :                           # 델타 탐색을 한바퀴 해가지고
            di, dj = i+dx, j+dy
            if visit[di][dj] == 1 :                 # 꽃잎 자리에 다른 꽃이 있다면
                backtrack(i,j+1,cnt,value)          # 다음 위치 백트래킹
                return
        for dx,dy in dr :                           # 위에서 return 되지 않았다면
            di,dj = i+dx, j+dy                      
            value += arr[di][dj]                    
            visit[di][dj] = 1                       # 그 자리를 꽃으로 채우고 값 더해두기
        visit[i][j] = 1                             # 중간 자리도 채우고
        value += arr[i][j]                          # 중간 값도 더하고

        backtrack(i,j+1,cnt-1,value)                # 백트래킹

        for dx,dy in dr :                           # 값 원위치 
            di,dj = i+dx, j+dy
            visit[di][dj] = 0 
        visit[i][j] = 0
        value = tmp                             

    backtrack(i,j+1,cnt,value)                      # 백트래킹



N = int(input())
arr = [ [*map(int,input().split())] for _ in range(N) ]
visit = [[0]*N for _ in range(N)]

ans = float('inf')

backtrack()

print(ans)