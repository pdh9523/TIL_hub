# stdin 사용하기
from sys import stdin


t = int(input())
test_list = []
for _ in range(t) :

    test_case = stdin.readline().strip('\n')
    if "push" in test_case :
        test_case = test_case.split()
        test_list.append(test_case[1])

    elif test_case == "top" :
        if len(test_list) > 0 :
            print(test_list[-1])
        else :
            print(-1)

    elif test_case == "size" :
        print(len(test_list))

    elif test_case == "empty" :
        if len(test_list) == 0 :
            print(1)
        else :
            print(0)

    elif test_case == "pop" :
        if len(test_list) >0 :
            print(test_list.pop())
        else :
            print(-1)