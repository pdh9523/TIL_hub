for i in range(1,11) :
    length, test_case = input().split()
    test_case = list(test_case)
    length = int(length)

    while True :
        count = True
        for idx in range(len(test_case)-1) :
            if test_case[idx] == test_case[idx+1] :
                test_case.pop(idx) # idx pop 두번 하면 idx , idx+1 둘다 빠짐 (중복 제거)
                test_case.pop(idx)
                count = False # 변경점 이 있으면 count를 false로 두어 아래의 중단 조건을 피함
                break # 새로 다시 while문 처음부터 돌리기
        if count :
            break # 변경점이 없으면 while문 중단
    print(f"#{i} ", *test_case, sep="")