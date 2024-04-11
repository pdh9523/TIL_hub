for _ in range(10) :
    t = int(input())
    test_list = []
    for _ in range(100) :
        test = list(map(int,input().split()))
        test_list.append(test)

    x = test.index(2) # x 좌표
    y = 99 # y 좌표

    while y > 0 :
        if x == 0 : # 0 인 경우 (일반적으로 돌리면 오류나서..)
            if test_list[y][x+1] == 1: # 오른쪽에 길이 있으면
                while x < 99 and test_list[y][x+1] == 1 : # 오른쪽에 길이 없을때까지
                    x += 1
        elif x == 99 : # 99 인 경우 
            if test_list[y][x-1] == 1 : #왼쪽에 길이 있으면
                while x > 0 and test_list[y][x-1] == 1 : # 왼쪽에 길이 없을때까지 
                    x -= 1
        elif test_list[y][x-1] == 1 : #왼쪽에 길이 있으면
            while x > 0 and test_list[y][x-1] == 1 : # 왼쪽에 길이 없을때까지 
                x -= 1
        elif test_list[y][x+1] == 1: # 오른쪽에 길이 있으면
            while x < 99 and test_list[y][x+1] == 1 : # 오른쪽에 길이 없을때까지
                x += 1
        y -= 1
    print(f"#{t} {x}")