a = input()

open_list=["[","("]

while a != "." :    # 종료조건 : 입력값이 "." 일 때

    test_list=[]
    # a의 모든 철자를 순회하면서
    for char in a :     
        if char in open_list :  # ( [ 가 있으면 리스트에 더하고,
            test_list.append(char)
        elif char == "]" :      # ] 가 나오면, 정상적인 조건이 아닌 경우 no를 출력하고 중단한다.
            if len(test_list) == 0 or test_list[-1] != "[" :
                print("no")
                break
            else :
                test_list.pop() # 정상적인 조건의 경우 pop 하고 계속 순회

        elif char == ")" :
            if len(test_list) == 0 or test_list[-1] != "(" :
                print("no")
                break
            else :
                test_list.pop()
    else :  # for 문을 정상적으로 순회한 후
        if len(test_list) == 0 :    # len == 0 인 경우 yes를, 아닌 경우 no를 출력한다.
            print("yes")
        else :
            print("no")

    a=input()   # 다시 돌려야함