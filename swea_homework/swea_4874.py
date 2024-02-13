t = int(input())
for i in range(t) :
    test_list = input().strip(".").split()  # 뒤의 . 를 제거하고 리스트 형태로 입력을 받음

    stack = []
    try :
        for char in test_list :
            if char.isdecimal() :           # 숫자인 경우 append
                stack.append(char)  
            else:                           # 연산자인 경우 
                b = float(stack.pop())      # 2개의 값을 스택에서 pop하고 연산
                a = float(stack.pop())
                if char == "+" :
                    stack.append(a+b)
                if char == "-" :
                    stack.append(a-b)
                if char == "*" :
                    stack.append(a*b)
                if char == "/" :
                    if b == 0 :             # 경우 3) 0 나눗셈 에러
                        print(f"#{i+1} error")
                        break
                    stack.append(a/b)
        if len(stack) != 1 :                # 경우 1) 연산자가 적어 스택에 숫자가 남아있는 경우
            print(f"#{i+1} error")
        else :                              # 올바른 경우) 스택에 값이 한개만 남은 경우 
            if stack[0] == int(stack[0]) :
                print(f"#{i+1} {int(stack[0])}")    # / 연산이 없는 경우나 나누어 떨어지는 경우 int 그대로 출력
            else :
                print(f"#{i+1} {stack[0]}")         # / 연산 중 소수점 발생 시 float 그대로 출력
    except IndexError :                     # 경우 2) 연산자가 많아 스택에 숫자가 남아 있지 않은 경우
        print(f"#{i+1} error")