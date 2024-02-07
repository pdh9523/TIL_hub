t = int(input())    

for idx in range(t) :
    test_case = input()     
    stack = [None] * len(test_case)   # stack의 최대치는 문자열의 길이
    
    top = -1    # stack을 위한 top 

    for char in test_case :
        # top = -1. 비어있거나, 맨 위의 철자가 char와 다를 경우
        if top == -1 or char != stack[top] :
            top += 1    # top 1칸 더 올리고
            stack[top] = char   # 그 위에 char를 쌓는다

        elif char == stack[top] :   # char가 스택의 peek와 같은 경우
            top -= 1    # top을 1칸 내린다
    print(f"#{idx+1} {top+1}")  # top의 바닥이 -1 이라 길이를 출력하려면 top에서 하나 올려서 출력