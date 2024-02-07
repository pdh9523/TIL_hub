t = int(input())

for i in range(t) :

    test_case = input()

    in_list = ["(", "{"]    # 괄호를 여는 경우
    result = 1

    test_list = []
    for char in test_case :
        if char in in_list :    # 괄호를 여는 경우에만 test_list에 담습니다.
            test_list.append(char)
        if char == "}" :    # 중괄호를 닫는 경우, 
            if len(test_list) == 0 or test_list[-1] == "(" :    # 리스트 안이 비었거나 리스트의 끝이 중괄호가 아니면
                result = 0  # 잘못된겁니다.
                break
            else :
                test_list.pop()    # 올바르게 된 경우 리스트의 마지막 값을 제거합니다.
        if char == ")" :    # 소괄호를 닫는 경우
            if len(test_list) == 0 or test_list[-1] == "{" :    # 리스트 안이 비었거나 리스트의 끝이 소괄호가 아니면
                result = 0  # 잘못된겁니다.
                break
            else :  # 올바르게 된 경우 리스트의 마지막 값을 제거합니다.
                test_list.pop()

    if len(test_list) >0 :  # 모든 리스트를 순회한 후 test_list에 남아 있으면 
        result=0    # 잘못된겁니다.
    print(f"#{i+1} {result}")   # 출력