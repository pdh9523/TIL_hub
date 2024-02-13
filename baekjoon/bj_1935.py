t = int(input())

test_case = list(input())

for i in range(t) :
    target = chr(65+i)
    rep = input()
    for idx in range(len(test_case)) :
        if test_case[idx] == target :
            test_case[idx] = rep



stack = []
for char in test_case :
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
            stack.append(a/b)

print("{:.2f}".format(stack[0]))