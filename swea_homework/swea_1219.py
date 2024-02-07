import sys
sys.stdin = open("1219.txt")

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
    result = 0    # 결과에 대한 변수
    checker = False     # 체커 (while 동작조건을 len(stack)!=0 으로 두려 했으나 초기값에 막혀서, 첫 시행을 한 이후부터 작동할 수 있도록 두었습니다.)
    while True :
        location = min(test_dict[idx])  # 위치를 idx에 담긴 value의 작은 값부터 순회
        stack.append(location)   # 찍었으니 스택에 담고
        test_dict[idx].remove(location)  # 한번 찍은 길은 딕셔너리에서 제거
        idx = location  # 이후의 탐색에서 다시 위치를 인덱스로 탐색
        if idx == 99 :  # 인덱스가 99? 
            result = 1   # 성공
            break

        while idx not in test_dict or test_dict[idx] == [] :    # 더이상 길이 없다
            
            if len(stack) == 0 :    # 근데 심지어 스택도 다 비었다
                checker = True      # 탐색 종료
                break

            else :
                idx = stack.pop()   # 길이 없으면 idx를 이전에 돌아왔던 길로 사용한다.

        if checker :    # 탐색 종료 시 while문도 같이 끈다.
            break

    print(f"#{t} {result}")
