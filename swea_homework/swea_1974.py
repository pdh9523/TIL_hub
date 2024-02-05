t = int(input())
check = {1,2,3,4,5,6,7,8,9}

for tc in range(t) :
    result = 1
    test_list = [list(map(int,input().split())) for _ in range(9)]
    tilted_list = [ list(char) for char in zip(*test_list)]

    # 가로열 검증
    for idx in range(9) :   
        if len(check - set(test_list[idx])) != 0 :
            result = 0

    # 세로열 검증
    for idx in range(9) :   
        if len(check - set(tilted_list[idx])) != 0 :
            result = 0

    # 3*3 검증
    for i in range(3) :
        for l in range(3) :
            rem = []
            for j in range(i*3, i*3 + 3) :
                for k in range(l*3, l*3 + 3) :
                    rem.append(test_list[j][k])
            if len(check - set(rem)) != 0 :
                result = 0
            
    print(f"#{tc+1} {result}")