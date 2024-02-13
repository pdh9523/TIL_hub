weight = {"+" : 1,
            "-" : 1,
            "*" : 2,
            "/" : 2,
            ")" : 0,
            "(" : 3
            }

stack_weight = {"+" : 1,
            "-" : 1,
            "*" : 2,
            "/" : 2,
            ")" : 0,
            "(" : 0   # 스택 내부에서 "(" 는 가장 낮은 우선순위로 움직이되, ")"를 만나면 괄호가 닫힐때까지 stack을 pop한다.
            }

for i in range(1,11) :

    t = int(input())

    test_case = input()

    test_list = []
    
    # 식 분리
    rem = ""
    for char in test_case :
        if char not in weight:
            rem += char
    
        else :
            if len(rem) > 0 :
                test_list.append(rem)
            test_list.append(char)
            rem = ""
    
    if len(rem) > 0 :
        test_list.append(rem) # 분리 완
    
    stack = []
    
    result = []     # 후위계산식이 담길 리스트
    for num in test_list :
        if num not in weight : 
            result.append(num)
        else :

            if num == ")":  # 우선순위인 이유 : elif 계산을 먼저 두면 괄호가 사칙연산처럼 계산되어 빠져나가게된다.
                while stack[-1] != "(" :
                    result.append(stack.pop())
                stack.pop()
                
            elif len(stack)>0 and weight[num] <= stack_weight[stack[-1]] :  # len(stack) > 0 를 넣은 이유 : 단축평가
                while len(stack) != 0 and weight[num] <= stack_weight[stack[-1]] : 
                    result.append(stack.pop())  # 스택의 마지막 값의 가중치가 지금 계산중인 값의 가중치보다 작아질때까지 pop하고 result에 더함
                stack.append(num)

            else :
                stack.append(num)
    while stack :   # 나머지 털기
        result.append(stack.pop())
    print(*result)
    result_stack = []
    for char in result :
        if char in weight :
            # result_stack.append(str(eval(f"{result_stack.pop()}{char}{result_stack.pop()}")))
            # eval 을 사용할 수 있지만, 여기선 안되니까 풀어씀
            b = float(result_stack.pop())	# 뒤의 값이 먼저 나온다
            a = float(result_stack.pop())
            if char == "+":
                result_stack.append(a+b)
            elif char == "-" :
                result_stack.append(a-b)
            elif char == "/" :
                result_stack.append(a/b)
            elif char == "*" :
                result_stack.append(a*b)
        else :
            result_stack.append(char)

    # 나눗셈의 경우가 주어지지 않아 필요는 없지만, 정수형과 값이 같은 경우 형변환
    if result_stack[0] == int(result_stack[0]) :
        print(f"#{i} {int(result_stack[0])}")
    else :
        print(f"#{i} {result_stack[0]}")