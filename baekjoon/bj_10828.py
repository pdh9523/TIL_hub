# stdin 사용하기
from sys import stdin


t = int(input())
test_list = []
for _ in range(t) :

    test_case = stdin.readline().strip('\n')    # 내용 많을까봐 readline() 으로 입력 받음
    if "push" in test_case :       # 푸쉬는
        test_case = test_case.split()   # 떼서
        test_list.append(test_case[1])  # 뒤의 값을 스택에 넣는다

    elif test_case == "top" :   # top은 
        if len(test_list) > 0 : # 리스트에 든게 있는 경우
            print(test_list[-1])    # 맨 위의 값을 출력한다.
        else :
            print(-1)   # 든게 없으면 -1

    elif test_case == "size" :  # size는
        print(len(test_list)) # 길이

    elif test_case == "empty" : # empty는
        if len(test_list) == 0 :    # 비어있는 경우 1, 아니면 0 출력
            print(1)
        else :
            print(0)

    elif test_case == "pop" :   # pop은
        if len(test_list) >0 :  # 리스트에 든게 있는 경우
            print(test_list.pop())  # pop하고 값을 출력
        else :
            print(-1)   # 비어있으면 -1