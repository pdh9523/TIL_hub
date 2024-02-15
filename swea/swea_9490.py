t = int(input())

for i in range(t) :
    n,m = map(int,input().split()) 
    test_list = [list(map(int, input().split())) for _ in range(n)] # 2차원 리스트

    x_sight = [1, 0, -1, 0] # 4방향으로 뻗을 때 쓸 리스트
    y_sight = [0, 1, 0, -1]

    sum_list = [] 
    for y in range(n) : #각 x,y값에서
        for x in range(m) :
            pang = test_list[y][x] # 풍선팡 할 풍선 고르고
            sum = pang # sum 값에 투입
            for weight in range(1,pang+1) : # 1부터 pang 까지 가중치를 주고
                for j in range(4) : # 4방향 돌려야되니까 4개
                    x_idx = x + (x_sight[j]*weight)
                    y_idx = y + (y_sight[j]*weight)
                    if 0 <= x_idx < m and 0 <= y_idx < n : # 인덱스 에러 검증
                        sum += test_list[y_idx][x_idx] # pang이 4라면 4방향 돌려서 총 16개의 값이 더해지는 방식
            sum_list.append(sum) # sum_list에 담고 max 값 추출
    print(f"#{i+1} {max(sum_list)}")
# 남의 코드 뺏은거니까 이 방식 몇 번 더 써보기