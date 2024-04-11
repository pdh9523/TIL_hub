dx, dy = [1,0,-1,0],[0,1,0,-1]

lands = []

nums = {0}

t =int(input())

for _ in range(t):
    land = list(map(int,input().split()))
    lands.append(land)
    nums.update(set(land))


max_value = 0 

# num을 기준으로 그 값을 초과한 값만 순회하면서 dfs로 조각 개수를 탐색
for num in nums :
    visit = [[0] *t for _ in range(t)]
    cnt = 0

    for i in range(t):
        for j in range(t):

            if not visit[i][j] and lands[i][j] > num:
                stack = [(i,j)]
                visit[i][j] = 1
                
                while stack :
                    x,y = stack.pop()       # 변수명 중복으로 쓰지 맙시다 (i,j 해서 5번 틀림)
                    for dt in range(4):
                        di = x + dx[dt]
                        dj = y + dy[dt]
                        if 0<= di < t and 0<= dj <t:
                            if visit[di][dj] == 0 and lands[di][dj] > num:
                                visit[di][dj] = 1
                                stack.append((di,dj))
                cnt+=1

    max_value = max(max_value,cnt)

print(max_value)