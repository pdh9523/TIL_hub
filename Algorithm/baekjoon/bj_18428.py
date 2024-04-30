# 감시를 피했는지 여부에 대한 함수
def check () :
    for i in range(N):
        for j in range(N):
            x,y = i,j
            if arr[x][y] == "S":
                # 가로열에 방해물을 설치했는가 ?
                for d in -1,1 :
                    while 0 <= x < N :
                        if arr[x][y] == "O":
                            break
                        if arr[x][y] == "T":
                            return False
                        x += d
                    x = i
                # 세로열에 방해물을 설치했는가 ?
                for d in -1,1:
                    while 0 <= y < N :
                        if arr[x][y] == "O":
                            break
                        if arr[x][y] == "T":
                            return False
                        y += d
                    y = j
    # return 안당했으면 체크 완료
    return True


# 백트래킹 함수 정의
def backtrack(i=0,j=0, cnt=3):
    if i == N-1 and j == N :
        if cnt == 0 and check():
            # check()를 통과했으면 exit
            exit(print("YES"))
        return

    if j == N :
        i += 1
        j = 0
    
    if arr[i][j] == "X" and cnt:
        arr[i][j] = "O"
        backtrack(i,j+1,cnt-1)
        arr[i][j] = "X"
    backtrack(i,j+1,cnt)


# 입력
N = int(input())
arr = [ input().split() for _ in range(N) ]

#출력
backtrack()
# 위에서 exit 안됐으면 "NO"출력
print("NO")