dr = (1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)

for tc in range(int(input())):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] =="*":
                continue
            cnt = 0
            for dx,dy in dr:
                di,dj = i+dx,j+dy
                if 0<=di<N and 0<=dj<N:
                    if arr[di][dj] =="*":
                        cnt +=1
            arr[i][j] = cnt
    ans = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] ==0:
                stack = [(i,j)]
                arr[i][j]="*"
                while stack:
                    x,y = stack.pop()

                    for dx,dy in dr:
                        di,dj = x+dx,y+dy
                        if 0<=di<N and 0<=dj<N and arr[di][dj] !="*":
                            if arr[di][dj] == 0:
                                stack.append((di,dj))
                            arr[di][dj] = "*"
                ans += 1
    for i in range(N):
        for j in range(N):
            if str(arr[i][j]).isnumeric():
                ans += 1

    print(f"{tc+1} {ans}")