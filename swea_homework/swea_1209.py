for _ in range(10) :

    t = int(input())
    test_list = []
    sum_list = []
    for _ in range(100) :
        test = list(map(int,input().split())) # 일차원 리스트
        test_list.append(test) # 이차원 리스트
        sum_list.append(sum(test)) # 그걸 더한 리스트(가로열 덧셈)
    output = 0
    for x in range(100) :
        output += test_list[x][x] # 대각선 정방향
    sum_list.append(output)
    output = 0
    for y in range(100) :
            output += test_list[99-y][y] # 대각선 역방향
            sum_list.append(output)
    
    for x in range(100) :
        output = 0
        for y in range(100) :
            output += test_list[y][x] # 세로열 덧셈
        sum_list.append(output)
    print(f"#{t} {max(sum_list)}")