t = int(input())
calc = ["*", "/", "+", "-"]
for _ in range(t) :
    stack = [] 
    test_case = input().split()
    for char in test_case :
        if char.isnumeric() :
            stack.append(int(char))
        elif char in calc :
            eval(stack.pop(), char, stack.pop())
    