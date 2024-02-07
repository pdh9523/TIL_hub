t = int(input())

for idx in range(t) :
    stack = []
    test_case = input()

    for char in test_case :
        if len(stack)==0 or char != stack[-1] :
            stack.append(char)
        elif char == stack[-1] :
            stack.pop()
        
    print(f"#{idx+1} {len(stack)}")