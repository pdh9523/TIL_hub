for idx in range(1,11) :    # 10개의 테스트 케이스
    _, password = input().split()   # 앞의 변수는 필요없으니 뒤의 password만 변수로 지정
    stack = []      # 리스트 할당
    for char in password :      # 문자열을 순회하면서
        if len(stack) == 0 or stack[-1] != char :   # 스택이 비어있거나, 마지막 항목이 비교하는 철자와 다를 경우
            stack.append(char)     # 리스트 뒤에 추가
        elif stack[-1] == char :    # 마지막 항목이 비교하는 철자와 같을 경우
            stack.pop()     # 리스트의 마지막 값을 제거
    print(f"#{idx}", "".join(stack))    # join으로 값을 합치고 인덱스와 함께 출력