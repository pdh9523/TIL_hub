import sys
input = sys.stdin.readline

dr = (1,0),(0,1),(-1,0),(0,-1)

def backtrack(i,j,total,idx=1):
    global ans
    
    if idx==4:
        ans = max(ans,total)
        return
    
    if total+maxv*(4-idx) <= ans:
        return
    
    for dx,dy in dr:
        di,dj = i+dx, j+dy
        if 0<=di<N and 0<=dj<M and not visit[di][dj]:
            visit[di][dj]=1
            # ㅗ 블럭을 만들기 위해 2번쨰에서 블럭 한번 고정
            if idx==2:
                backtrack(i,j,total+arr[di][dj],idx+1)
            
            backtrack(di,dj,total+arr[di][dj],idx+1)
            visit[di][dj]=0

N,M = map(int,input().split())
arr = [[*map(int,input().split())] for _ in range(N)] 

visit = [[0]*M for _ in range(N)]
maxv= max(map(max,arr))
ans = 0
for i in range(N):
    for j in range(M):
        visit[i][j]=1
        backtrack(i,j,arr[i][j])
        visit[i][j]=0

print(ans)