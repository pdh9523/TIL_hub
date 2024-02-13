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
print(*result, sep="")
