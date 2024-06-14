from collections import deque
dr = (0,1),(1,0),(-1,0),(0,-1)

def bfs(data):
    arr = [[0]*5 for _ in range(5)]
    for i in data :
        x,y = i//5, i%5
        arr[x][y] = 1
    
    q = deque([(x,y)])
    while q :
        x,y=q.popleft()

        for dx,dy in dr:
            di,dj =x+dx,y+dy
            if 0<=di<5 and 0<=dj<5:
                if arr[di][dj]:
                    arr[di][dj]=0
                    q.append((di,dj))

    return sum([sum(row) for row in arr])

# 전역 탐색을 통해 모든 경우의 수를 찾고,
def backtrack(i=0,idx=0,som=0,visit=[]):
    global ans

    if idx ==7:
        if som >= 4:
            # bfs를 통해 서로 붙어있는지 확인하여
            if not bfs(visit):
                # 값을 계산
                ans += 1
        return
    
    if i == 25 :
        return
    
    if idx >= 4 and som < idx-3:
        return

    x,y = i//5, i%5
    if arr[x][y] == "S":
        backtrack(i+1,idx+1,som+1,visit+[i])
    else :
        backtrack(i+1,idx+1,som,visit+[i])
    backtrack(i+1,idx,som,visit)


dr = (0,1),(1,0),(0,-1),(-1,0)
arr = [ list(input()) for _ in range(5) ]
ans = 0
backtrack()
print(ans)