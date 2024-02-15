import sys
sys.stdin = open("4615.txt")

# 1이 흑돌, 2가 백돌
di = [0,1,0,-1,1,-1,1,-1]
dj = [1,0,-1,0,1,-1,-1,1]
# 가중치는 N 값으로 할당

t = int(input())

for idx in range(t) :
    N,M = map(int,input().split())
    test_list = [[0 for _ in range(N)] for _ in range(N)]
    test_list[N//2][N//2] = 2
    test_list[N//2-1][N//2-1] = 2
    test_list[N//2-1][N//2] = 1
    test_list[N//2][N//2-1] = 1
    # 오셀로 판 완성
    
    for _ in range(M) :
        x,y,color = map(int,input().split())
        x-=1    # 좌표 보정
        y-=1
        test_list[x][y] = color
        for delta in range(8) :     # 델타 탐색
            i = x + di[delta]
            j = y + dj[delta]
            visit = []

            while 0 <= i < N and 0 <= j < N :
                if test_list[i][j] == 0 :   # 0이면 바로 break
                    break
                elif test_list[i][j] == color : # color를 만나면
                    for ii, jj in visit :       # visit에 담겨 있던 모든 좌표를 색칠
                        test_list[ii][jj] = color
                    break
                else :                  # 둘다 아니면 visit에 담아두기
                    visit.append([i,j])
                i += di[delta]  # 델타 값을 올리면서 진행
                j += dj[delta]



    b_count = 0
    w_count = 0
    # 1이 흑돌, 2가 백돌
    for tls in test_list :
        b_count += tls.count(1)
        w_count += tls.count(2)
    print(f"#{idx+1} {b_count} {w_count}")