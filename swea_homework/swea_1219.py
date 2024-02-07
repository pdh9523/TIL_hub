for _ in range(10) :    # 테케 10개
    t, test_case = map(int,input().split()) 

    test_list = list(map(int,input().split()))
    test_dict = {}  # 딕셔너리로 정렬
    for idx in range(0,len(test_list),2) :  # 2개씩 넘어가면서 
        if test_list[idx] not in test_dict :    # 홀수열은 키로, 짝수열은 벨류로 받음
            test_dict[test_list[idx]] = [test_list[idx+1]]
        else :
            test_dict[test_list[idx]].append(test_list[idx+1])
        
    stack = []  # 스택 리스트
    idx = 0     # 현재 인덱스 (인덱스에서 전처리를 하고 위치를 바꿔야한다.)
    location = 0    # 현재 위치

    result = 1    # 결과에 대한 변수
    while result == 1 :
        location = min(test_dict[idx])  # 위치를 idx에 담긴 value의 작은 값부터 순회
        stack.append(location)   # 찍었으니 스택에 담고
        test_dict[idx].remove(location)  # 한번 찍은 길은 딕셔너리에서 제거
        idx = location  # 이후의 탐색에서 다시 위치를 인덱스로 탐색

        if idx == 99 :  # 인덱스가 99? 
            break   # 끝

        while idx not in test_dict or test_dict[idx] == [] :    # 더이상 길이 없다
            if len(stack) == 0 :    # 근데 심지어 스택도 다 비었다
                result = 0      # result를 0으로 바꾸고 while도 종료한다.
                break
            else :  # 스택에 있긴 하다
                idx = stack.pop()   # idx를 직전에 갔던 길로 사용한다.

    print(f"#{t} {result}")
