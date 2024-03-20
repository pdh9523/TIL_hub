from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

R,C = map(int,input().split())  # R 세로 C 가로

forests = []
stars=[]
for i in range(R):
    forest = list(input())
    for idx,char in enumerate(forest):
        if char == "S":
            S = (i,idx)
        elif char == "D":
            D = (i,idx)
        elif char == "*":
            stars.append((i,idx))
    forests.append(forest)

q = deque([S])
visit = [[0]*C for _ in range(R)]
check = []

for dt in range(4):
    Di = D[0] + dx[dt]
    Dj = D[1] + dy[dt]
    if 0 <= Di < R and 0 <= Dj < C:
        if forests[Di][Dj] not in "X*":
            forests[Di][Dj] = "DD"

visit[S[0]][S[1]] = 1

while q :
    i,j = q.popleft()

    if forests[i][j] in stars:
        continue

    if forests[i][j] == "D" or forests[i][j] == "DD":
        print(visit[i][j])
        break

    if visit[i][j] not in check:
        tmp = []
        for si,sj in stars :
            for dt in range(4):
                ri = si+dx[dt]
                rj = sj+dy[dt]
                if 0 <= ri < R and 0 <= rj < C :
                    if forests[ri][rj] not in "*XD":
                        forests[ri][rj] = "*"
                        tmp.append((ri,rj))
                        if (ri,rj) in q :
                            q.remove((ri,rj))
        check.append(visit[i][j])
        stars.extend(tmp)

    for dt in range(4):
        di = i + dx[dt]
        dj = j + dy[dt]
        if 0 <= di < R and 0 <= dj < C :
            if not visit[di][dj] and forests[di][dj] not in "X*" :
                q.append((di,dj))
                visit[di][dj] = visit[i][j] + 1    


else :
    print("KAKTUS")