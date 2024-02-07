for idx in range(1,11) :    # 10개의 테스트 케이스
    num, password = input().split()   # 문자열의 길이는 num, 뒤의 비밀번호는 password
    stack = [None] * int(num)      # 문자열의 길이가 스택의 최대 길이가 된다.
    top = -1    # top은 우선 -1 할당
    for char in password :      # 문자열을 순회하면서
        if top == -1 or stack[top] != char :   # 스택이 비어있거나, 마지막 항목이 비교하는 철자와 다를 경우
            top += 1
            stack[top] = char     # 리스트 뒤에 추가
        elif stack[top] == char :    # 마지막 항목이 비교하는 철자와 같을 경우
            top -= 1     # 리스트의 마지막 값을 제거
    print(f"#{idx}", "".join(stack[:top+1]))    # join으로 값을 합치고 인덱스와 함께 출력