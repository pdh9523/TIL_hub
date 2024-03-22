# 리스트를 굳이 써야할까? 2000*2000 하면 꽤 넓은데
# 시뮬레이션 문제면 조건 내에서 좌표만 신경써서 풀이해보기

# 0 : 상 1 : 하 2 : 좌 3 : 우

dx = [-1,1,0,0]
dy = [0,0,-1,1]


for tc in range(1,int(input())+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)] 
    # arr [0] : x좌표 [1] : y좌표 [2] : 방향 [3] : 에너지

    ans = 0

    while len(arr) < 2 :        # 원자가 다 없어질때까지 (하나 이하로 남기)
        for ele in arr :        # 시뮬레이션의 각 원자에서
            dr = arr[2]         # 방향을 델타로 정해두고 
            ele[0] += dx[dr]    # 더해주기
            ele[1] += dy[dr]
    # 움직인 이후의 조건 : 1) 범위를 벗어났는가? 2) 부딪혔는가?
            if not -1000 <= ele[0] <= 1000 and not -1000 <= ele[1] <= 1000 :
                arr.remove(ele)
        # '부딪혔는가' 에 대한 조건
        for 