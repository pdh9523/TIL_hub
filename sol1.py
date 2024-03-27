N = int(input())
text = input()  

if N%2 == 1 :                       # 홀수인 경우
    exit(print("No"))               # 탐색 실패
    
need_open = N//2 - text.count("(")  # need_open : 필요한 여는 괄호의 수 

stack = []                          
for char in text:                   # 스택을 활용해 순회
    if char == "(":                 # 여는 괄호의 경우 스택에 더함
        stack.append(char)
    elif char == ")":               # 닫는 괄호의 경우 
        if stack :                  # 스택이 있으면
            stack.pop()             # 하나 뺌
        else :                      # 스택이 비어있으면
            exit(print("No"))       # 탐색 실패

    elif char == "?":               # 물음표의 경우
        if need_open:               # 필요한 여는 괄호의 수가 남아 있는 경우
            stack.append("(")       # 여는 괄호에 더함
            need_open -= 1          # 필요한 수 줄임
        else :                      # 여는 괄호의 수가 남아 있지 않은 경우
            stack.pop()             # 닫기

if stack :                          # 순회 종료 후 스택에 남아 있으면                        
    print("No")                     # 탐색 실패
else :                              # 스택이 비어있으면
    print("Yes")                    # 탐색 완료 